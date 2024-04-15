import socket
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io import wavfile
import numpy as np


# Creating a socket instance
# AF_INET : Work with address family of IP V4
# SOCK_STREAM: Accept TCP packets (SOCK_DGRAM is for UDP)
client_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Connecting to the localhost
ip_address = '127.0.0.1'
port = 5555
request_state = True

# Client request to the server
client_object.connect((ip_address,port))

# receiving response from server
data_receive = client_object.recv(1024)

if request_state == True:
    
    # if response is not null
    if data_receive:
 	    # Connection is successful
        print("CLIENT CONNECTED TO SERVER")
        # print(data_receive.decode('utf-8'))
        
        while data_receive:
    	   
           # sound input
            sample_rate, audio_data = wavfile.read('audio.wav')
           
           # sending request to the server
           # print(f"the original sample rate is {bin(sample_rate)}")
            client_object.send(bin(sample_rate).encode())
            client_object.send(bin(audio_data.size).encode())
            # print(f"the original sample rate is {audio_data.size}")
            print("Sending!!")
            client_object.send(audio_data.tobytes())
            # client_object.send((b"stop"))
            # receiving response from the server
            # data_receive = client_object.recv(1024)
            # if data_receive:
            #     print("{}: {}".format("SERVER",data_receive.decode('utf-8')))