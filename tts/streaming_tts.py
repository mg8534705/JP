from TTS.api import TTS

class StreamingTTS:
    def __init__(self):
        self.tts = TTS(model_name="tts_models/en/ljspeech/fastspeech2", progress_bar=False, gpu=True)

    def stream_synthesize(self, text, output_path="output.wav"):
        self.tts.tts_to_file(text=text, file_path=output_path)
        return output_path
