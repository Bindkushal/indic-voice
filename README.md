# IndicVoice

A Decoder-Only Neural TTS system with Native G2P for Indian Languages.

**Author:** Kushal Kant Bind  
**Affiliation:** Department of Mathematics, Chandigarh University  
**Project:** IndicVoice Research — Part of GSoC 2025, Sugar Labs  
**Contact:** bindkushalkant@gmail.com

---

## Overview

IndicVoice extends the Kokoro-82M TTS architecture for Indian languages, replacing the default G2P engine with [indic-g2p](https://github.com/Bindkushal/indic-g2p) — a native Grapheme-to-Phoneme engine built for Devanagari, Gurmukhi, Bengali, and other Indic scripts.

## Supported Languages

| Code | Language | Script | Status |
|------|----------|--------|--------|
| hi | Hindi | Devanagari | ✅ Ready |
| pa | Punjabi | Gurmukhi | ✅ Ready |
| bn | Bengali | Bengali | 🔧 Beta |
| en | English | Roman | ✅ Ready |
| ta, te, kn, mr, gu, or, ml, ur, as | Others | — | ⏳ Planned |

---

## Installation

```bash
pip install git+https://github.com/Bindkushal/indic-g2p.git
pip install git+https://github.com/Bindkushal/indic-voice.git
apt-get install espeak-ng
```

---

## Quick Start

```python
from indicvoice import IndicPipeline

pipeline = IndicPipeline(
    lang_code='hi',
    repo_id='Bindkushal/IndicVoice-82M'
)

for gs, ps, audio in pipeline('नमस्ते दुनिया', voice='af_heart'):
    print('Text:', gs)
    print('Phonemes:', ps)
    import soundfile as sf
    sf.write('output.wav', audio, 24000)
```

---

## Local Setup (with GPU)

### Requirements
- Python 3.9+
- CUDA 11.8+ (for GPU)
- espeak-ng

### Steps

```bash
# 1. Clone repos
git clone https://github.com/Bindkushal/indic-voice.git
git clone https://github.com/Bindkushal/indic-g2p.git

# 2. Install dependencies
apt-get install espeak-ng
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers soundfile loguru addict num2words phonemizer espeakng-loader

# 3. Install packages
pip install -e ./indic-g2p
pip install -e ./indic-voice

# 4. Set HF token
export HF_TOKEN=your_token_here

# 5. Test
python3 -c "
from indicvoice import IndicPipeline
pipeline = IndicPipeline(lang_code='hi', repo_id='Bindkushal/IndicVoice-82M')
for gs, ps, audio in pipeline('नमस्ते दुनिया', voice='af_heart'):
    import soundfile as sf
    sf.write('output.wav', audio, 24000)
    print('Saved output.wav')
    break
"
```

---

## Google Colab Setup

```python
# Cell 1 — Install
!apt-get -qq -y install espeak-ng > /dev/null 2>&1
!pip install -q soundfile huggingface_hub loguru regex numpy addict num2words phonemizer espeakng-loader transformers
!pip install -q --no-cache-dir git+https://github.com/Bindkushal/indic-g2p.git
!pip install -q --no-cache-dir git+https://github.com/Bindkushal/indic-voice.git

# Cell 2 — Set HF Token (add HF_TOKEN to Colab Secrets first)
from google.colab import userdata
import os
os.environ['HF_TOKEN'] = userdata.get('HF_TOKEN')

# Cell 3 — Load and Run
from indicvoice import IndicPipeline
from IPython.display import display, Audio
import soundfile as sf

pipeline = IndicPipeline(lang_code='hi', repo_id='Bindkushal/IndicVoice-82M')

for i, (gs, ps, audio) in enumerate(pipeline('नमस्ते दुनिया', voice='af_heart')):
    print('Text:', gs)
    print('Phonemes:', ps)
    display(Audio(data=audio, rate=24000))
    sf.write(f'output_{i}.wav', audio, 24000)
```

> **Note:** Use GPU runtime in Colab — Runtime → Change runtime type → T4 GPU

---

## Training on IndicVoices-R

IndicVoices-R is a 1700+ hour multilingual Indian TTS dataset by AI4Bharat.
Dataset: https://github.com/AI4Bharat/IndicVoices-R

### Download Hindi Data

```bash
wget https://indic-tts-public.objectstore.e2enetworks.net/data/ivr/Hindi.tar.gz
tar -xf Hindi.tar.gz
```

### Download IIT Madras Open Source Data

- IndicTTS Hindi: https://www.iitm.ac.in/donlab/tts/index.php
- License: CC BY 4.0

```bash
# After downloading IndicTTS
# Format data into LJSpeech format:
# metadata.csv: filename|text|normalized_text
# wavs/: 22050Hz mono WAV files
```

### Fine-tuning on Colab (T4 GPU)

```python
# Coming soon — Colab notebook for fine-tuning IndicVoice on Hindi data
# Target: fine-tune on 100hrs Hindi speech from IndicVoices-R
# Expected training time: ~8hrs on A100, ~24hrs on T4
```

---

## Architecture

- **Base:** Kokoro-82M (StyleTTS2 + ISTFTNet) — Apache 2.0
- **G2P:** indic-g2p — native Indic phonemizer
- **Training data:** IndicVoices-R + IIT Madras IndicTTS
- **Parameters:** 82M
- **Sample rate:** 24000 Hz

---

## Citation

```bibtex
@misc{bind2025indicvoice,
  title={IndicVoice: Decoder-Only Neural TTS with Native G2P for Indian Languages},
  author={Kushal Kant Bind},
  year={2025},
  institution={Chandigarh University},
  note={Part of GSoC 2025, Sugar Labs}
}
```

## Acknowledgements

- hexgrad/kokoro — base TTS architecture (Apache 2.0)
- AI4Bharat — IndicVoices-R dataset
- IIT Madras — IndicTTS dataset
- Sugar Labs — GSoC 2025

## License

Apache 2.0 — See LICENSE file.
