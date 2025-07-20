import queue
import sounddevice as sd
import numpy as np

class AudioStreamHandler:
    def __init__(self, samplerate=16000, chunk_duration=0.3):
        self.samplerate = samplerate
        self.chunk_size = int(chunk_duration * samplerate)
        self.q = queue.Queue()

    def callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.q.put(indata.copy())

    def start_input_stream(self):
        return sd.InputStream(samplerate=self.samplerate, channels=1, callback=self.callback)

    def get_audio_chunk(self):
        return self.q.get()

def play_audio(path):
    import soundfile as sf
    data, sr = sf.read(path)
    sd.play(data, sr)
    sd.wait()
