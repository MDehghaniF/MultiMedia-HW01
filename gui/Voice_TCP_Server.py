#Source from freecodecamp
# https://www.freecodecamp.org/news/socket-programming-in-python/

import socket
import random
import string
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io import wavfile
import numpy as np

# Creating a socket instance
# AF_INET : Work with address family of IP V4
# SOCK_STREAM: Accept TCP packets (SOCK_DGRAM is for UDP)
server_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Connecting to the localhost
ip_address = '127.0.0.1'
port = 5555
server_object.bind((ip_address, port))
server_object.listen()  


#Once the client connects to the particular port, the server starts to accept the request.
connection_object, _ = server_object.accept()

if connection_object:
	# Connected to client successfully
    print("SERVER CONNECTED TO CLIENT")
    
    # sending initial message to the client
    connection_object.send(b"send the sample rate")
    
    # receiving message from the client
    sample_rate = connection_object.recv(100)
    audio_size  = connection_object.recv(100)
    audio_data = connection_object.recv(1024)
    
    
    sample_rate = int(sample_rate.decode(),2)
    audio_size  = int(audio_size.decode(),2)
    # input_data  = np.array([0])
    input_data  = np.frombuffer(audio_data,dtype=np.float32)
    audio_data = connection_object.recv(1024)

    print(f"the recivied sample rate is {sample_rate}")
    print(f"the recivied sample rate is {audio_size}")
   

    while True :

        #  server_input = random.choice(string.ascii_letters)
        #  connection_object.send(server_input.encode('utf-8'))
        #  print("Reciving!!")
         audio_data = np.frombuffer(audio_data,dtype=np.float32)
         input_data = np.append(input_data, audio_data)
         print(f"The input size of data is {input_data.size}")
       
         audio_data = connection_object.recv(1024)
         
         
         if input_data.size >= audio_size:
             break
         
    write('captured_audio/Recieved_audio.wav', sample_rate, input_data)  # Save as WAV file 
    connection_object.close()   