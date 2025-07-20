
import streamlit as st
from asr.streaming_whisper_asr import StreamingWhisperASR
from nmt.incremental_mt5_translation import IncrementalMT5Translator
from tts.streaming_tts import StreamingTTS
from utils.japanese_utils import detect_honorific
import tempfile, time
import soundfile as sf
import os

st.set_page_config(page_title="JP-EN Real-Time S2ST", layout="centered")

st.title("🈺 Real-Time Japanese-English Speech-to-Speech Translator")
st.markdown("### 🎙️ Speak Japanese → 🧠 Transcribe → 🌐 Translate → 🗣️ Speak English")

# Upload or record audio
uploaded_file = st.file_uploader("Upload a Japanese audio file (WAV, 16kHz mono)", type=["wav"])

if uploaded_file:
    st.audio(uploaded_file, format="audio/wav")
    audio_data, sr = sf.read(uploaded_file)

    with st.spinner("Loading models..."):
        asr = StreamingWhisperASR(model_size="medium")
        translator = IncrementalMT5Translator()
        tts = StreamingTTS()

    with st.spinner("🔍 Transcribing..."):
        temp_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())

        jp_texts = asr.stream_transcribe(temp_path)
        jp_text = " ".join(jp_texts)
        st.text_area("📝 Transcription (Japanese)", value=jp_text, height=100)

    register = detect_honorific(jp_text)
    st.markdown(f"**Honorific Register:** `{register}`")

    with st.spinner("🌐 Translating..."):
        en_text = translator.translate_incremental(jp_text)
        st.text_area("🌍 Translation (English)", value=en_text, height=100)

    with st.spinner("🗣️ Synthesizing..."):
        out_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
        tts.stream_synthesize(en_text, out_path)

        st.audio(out_path, format="audio/wav")

    latency_ms = round((os.path.getmtime(out_path) - os.path.getctime(temp_path)) * 1000, 2)
    st.success(f"⚡ Latency (Approx): {latency_ms} ms")
else:
    st.info("Please upload a Japanese WAV file (mono, 16kHz).")
