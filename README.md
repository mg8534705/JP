# Real-Time Japanese-English Speech-to-Speech Translation (Phase 2)
Streaming-optimized version with sub-300ms latency goal.

## Components
- **Streaming ASR**: Faster-Whisper
- **Incremental NMT**: mT5 with SOV→SVO and honorific handling
- **Streaming TTS**: FastSpeech2 + HiFi-GAN
- **Full Streaming Audio I/O**

## How to Use
1. Install with `!pip install -r requirements.txt`
2. Run `main_colab_streaming_demo.ipynb`
