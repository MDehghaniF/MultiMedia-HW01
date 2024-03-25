#Source from freecodecamp
# https://www.freecodecamp.org/news/socket-programming-in-python/

import string
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io import wavfile
import numpy as np

sample_rate, audio_data = wavfile.read('sound/audio.wav')

source_file =  open("source.txt","w")
source_file.write(np.array2string(audio_data))
print(f"the size of source file is {audio_data.size}")
print(f"the dim of source file is {audio_data.ndim}")
source_file.close()

sample_rate, audio_data = wavfile.read('sound/server_audio.wav')

source_file =  open("recived.txt","w")
print(f"the size of received file is {audio_data.size}")
print(f"the dim of received file is {audio_data.ndim}")
source_file.write(np.array2string(audio_data))
source_file.close()