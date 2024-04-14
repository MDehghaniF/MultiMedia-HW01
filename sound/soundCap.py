import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io import wavfile
import numpy as np

def voice_record(fs = 44100, seconds = 30, name = 'captured_audio/audio.wav'):

    # fs = 44100  # Sample rate
    # seconds = 3  # Duration of recording
    # name = 'audio.wav'
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    print("recording!!!")
    sd.wait()  # Wait until recording is finished
    
    # print(myrecording)
    write(name, fs, myrecording)  # Save as WAV file ,
    print("End of recording")

def voice_play(name = 'captured_audio/audio.wav'):
    # name = 'audio.wav'
    # Load a WAV file (replace 'your_audio.wav' with the actual file path)
    sample_rate, audio_data = wavfile.read(name)

    # print ("this is a size of numpy array")
    # print(audio_data.dtype)
    # print("the size of the array is ",audio_data.dim())
    # Play the audio
    sd.play(audio_data, sample_rate)
    sd.wait()  # Wait until playback is finished

voice_record()
voice_play()