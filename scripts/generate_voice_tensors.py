"""
generate_voice_tensors.py
─────────────────────────
Run this ONCE locally to create placeholder voice .pt tensors
if you don't have them yet, OR to wrap your real voice embeddings
into the correct format for HuggingFace.

Usage (placeholder):
    python generate_voice_tensors.py --mode placeholder

Usage (wrap real embeddings — if you have a numpy/pt file):
    python generate_voice_tensors.py --mode real --source my_hi_female.npy --out voices/hi_female.pt

 voice tensor format:
    torch.Size([1, 1, style_dim])  →  style_dim = 128
"""

import argparse
import os
import torch

VOICES = {
    "hi_female": {"lang": "hi", "gender": "female"},
    "hi_male":   {"lang": "hi", "gender": "male"},
    "pa_female": {"lang": "pa", "gender": "female"},
    "pa_male":   {"lang": "pa", "gender": "male"},
    "bn_female": {"lang": "bn", "gender": "female"},
    "en_female": {"lang": "en", "gender": "female"},
}

STYLE_DIM = 128  # must match config.json style_dim


def make_placeholder(name: str, out_dir: str):
    """Create a zero-filled style tensor — replace with real embeddings later."""
    tensor = torch.zeros(1, 1, STYLE_DIM)
    path = os.path.join(out_dir, f"{name}.pt")
    torch.save(tensor, path)
    print(f"  [placeholder] saved {path}  shape={tuple(tensor.shape)}")


def wrap_real(source: str, out_path: str):
    """Wrap an existing numpy or .pt embedding into the correct shape."""
    if source.endswith(".npy"):
        import numpy as np
        arr = np.load(source)
        tensor = torch.from_numpy(arr).float()
    else:
        tensor = torch.load(source, weights_only=True).float()

    # Reshape to (1, 1, style_dim) if needed
    tensor = tensor.reshape(1, 1, STYLE_DIM)
    torch.save(tensor, out_path)
    print(f"  [real] saved {out_path}  shape={tuple(tensor.shape)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode",   choices=["placeholder", "real"], default="placeholder")
    parser.add_argument("--source", default=None,  help="Source .npy or .pt for --mode real")
    parser.add_argument("--voice",  default=None,  help="Voice name for --mode real, e.g. hi_female")
    parser.add_argument("--out_dir",default="voices", help="Output directory")
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    if args.mode == "placeholder":
        print(f"Creating placeholder voice tensors in ./{args.out_dir}/")
        for name in VOICES:
            make_placeholder(name, args.out_dir)
        print("\nDone. Replace these with real trained embeddings before final push.")
        print("Shape per file: torch.Size([1, 1, 128])")

    elif args.mode == "real":
        assert args.source, "--source required in real mode"
        assert args.voice,  "--voice required in real mode"
        out_path = os.path.join(args.out_dir, f"{args.voice}.pt")
        wrap_real(args.source, out_path)
