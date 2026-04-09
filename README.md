---
language:
  - hi
  - pa
  - bn
  - en
license: apache-2.0
tags:
  - text-to-speech
  - tts
  - indic
  - styletts2
pipeline_tag: text-to-speech
---

# IndicVoice

A decoder-only neural TTS model for Indian languages, built on the Kokoro-82M architecture with a native Indic G2P frontend.

**Author:** Kushal Kant Bind — Chandigarh University
**Project:** GSoC 2026, Sugar Labs
**GitHub:** [Bindkushal/indic-voice](https://github.com/Bindkushal/indic-voice)

---

## Quick Start

```bash
pip install git+https://github.com/Bindkushal/indic-g2p.git
pip install git+https://github.com/Bindkushal/indic-voice.git
apt-get install espeak-ng
```

```python
from indicvoice import IndicPipeline
pipeline = IndicPipeline(lang_code="hi", repo_id="Bindkushal/IndicVoice-82M")
for gs, ps, audio in pipeline("नमस्ते दुनिया", voice="af_heart"):
    import soundfile as sf
    sf.write("output.wav", audio, 24000)
```

---

## Files in This Repo

| File | Description |
|------|-------------|
| `config.json` | Model architecture config |
| `indicvoice-v1_0.pth` | Model weights (82M params) |
| `voices/af_heart.pt` | Default voice style tensor |
| `voices/af_bella.pt` | Voice style tensor |
| `voices/am_adam.pt` | Voice style tensor |

---

## Supported Languages

| Language | Code | Script | Status |
|----------|------|--------|--------|
| Hindi | `hi` | Devanagari | Ready |
| Punjabi | `pa` | Gurmukhi | Ready |
| Bengali | `bn` | Bengali | Beta |
| English | `en` | Roman | Ready |

---

## Architecture

- **Base:** Kokoro-82M (StyleTTS2 + ISTFTNet), Apache 2.0
- **G2P:** [indic-g2p](https://github.com/Bindkushal/indic-g2p) — native Indic phonemizer
- **Fallback:** espeak-ng for OOV words
- **Parameters:** 82M
- **Sample rate:** 24000 Hz

---

## Citation

```bibtex
@misc{bind2026indicvoice,
  title={IndicVoice: Decoder-Only Neural TTS with Native G2P for Indian Languages},
  author={Kushal Kant Bind},
  year={2026},
  institution={Chandigarh University},
  note={GSoC 2026, Sugar Labs}
}
```

## Acknowledgements

- [hexgrad/kokoro](https://github.com/hexgrad/kokoro) — base TTS architecture (Apache 2.0)
- AI4Bharat — IndicVoices-R dataset
- IIT Madras — IndicTTS dataset

## License

Apache 2.0
