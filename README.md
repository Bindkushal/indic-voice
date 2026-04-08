# IndicVoice

A Decoder-Only Neural TTS system with Native G2P for Indian Languages.

**Author:** Kushal Kant Bind  
**Affiliation:** Department of Mathematics, Chandigarh University  
**Project:** IndicVoice Research — Part of GSoC 2025, Sugar Labs

---

## Overview

IndicVoice extends the Kokoro TTS architecture for Indian languages, replacing the Misaki G2P engine with [indic-g2p](https://github.com/Bindkushal/indic-g2p) — a native Grapheme-to-Phoneme engine built for Devanagari, Gurmukhi, Bengali, and other Indic scripts.

## Supported Languages

| Code | Language | Script | Status |
|------|----------|--------|--------|
| hi | Hindi | Devanagari | ✅ Ready |
| pa | Punjabi | Gurmukhi | ✅ Ready |
| bn | Bengali | Bengali | 🔧 Beta |
| en | English | Roman | ✅ Ready |
| ta, te, kn, mr, gu, or, ml, ur, as | Others | — | ⏳ Planned |

## Quick Start
```python
from indicvoice import IndicPipeline

pipeline = IndicPipeline(lang_code='hi')
generator = pipeline('नमस्ते दुनिया', voice='hi_female')
for gs, ps, audio in generator:
    print(gs, ps)
```

## Architecture

- **Base model:** Kokoro-82M (hexgrad/kokoro) — Apache 2.0
- **G2P engine:** indic-g2p (native Indic phonemizer)
- **Training data:** IndicVoices-R dataset

## Citation
```bibtex
@misc{bind2025indicvoice,
  title={IndicVoice: Decoder-Only Neural TTS with Native G2P for Indian Languages},
  author={Kushal Kant Bind},
  year={2025},
  institution={Chandigarh University}
}
```

## License

Apache 2.0 — See LICENSE file.
