from faster_whisper import WhisperModel

class StreamingWhisperASR:
    def __init__(self, model_size='medium', compute_type="float16"):
        self.model = WhisperModel(model_size, compute_type=compute_type)

    def stream_transcribe(self, audio_chunk):
        segments, _ = self.model.transcribe(audio_chunk, language='ja', vad_filter=True)
        return [segment.text for segment in segments]
