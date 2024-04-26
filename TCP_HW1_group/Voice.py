import socket
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io import wavfile
from multiprocessing import Process
import time



def record(fs = 44100, seconds = 30, name = 'captured_audio/audio.wav'):

    # fs = 44100  # Sample rate
    # seconds = 3  # Duration of recording
    # name = 'audio.wav'
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    print("recording!!!")
    # sd.wait()  # Wait until recording is finished
    time.sleep(30)
    # wait function cuase to the not responding error while the record function is working!!
    
    # print(myrecording)
    write(name, fs, myrecording)  # Save as WAV file ,
    print("End of recording")

def play(name = 'captured_audio/Recieved_audio.wav'):
    # name = 'audio.wav'
    # Load a WAV file (replace 'your_audio.wav' with the actual file path)
    sample_rate, audio_data = wavfile.read(name)

    # Play the audio
    sd.play(audio_data, sample_rate)
    time.sleep(30)
    # sd.wait()  # Wait until playback is finished

def TCP_transmit(ip_address = '127.0.0.1', port = 5555):
    # Creating a socket instance
    # AF_INET : Work with address family of IP V4
    # SOCK_STREAM: Accept TCP packets (SOCK_DGRAM is for UDP)
    client_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # Connecting to the localhost
    # ip_address = '127.0.0.1'
    # port = 5555

    # Client request to the server
    client_object.connect((ip_address,port))

    # receiving response from server
    data_receive = client_object.recv(1024)

        
    # if response is not null
    if data_receive:
        # Connection is successful
        print("CLIENT CONNECTED TO SERVER")
        
        while data_receive:
        
        # sound input
            sample_rate, audio_data = wavfile.read('captured_audio/audio.wav')
        
        # sending request to the server
            client_object.send(bin(sample_rate).encode())
            client_object.send(bin(audio_data.size).encode())
            print("Sending!!")
            client_object.send(audio_data.tobytes())
            print("Before closing")
            client_object.close()


def voice_server(port = 6666):
    
   
    # Creating a socket instance
    # AF_INET : Work with address family of IP V4
    # SOCK_STREAM: Accept TCP packets (SOCK_DGRAM is for UDP)
    server_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # Connecting to the localhost
    host = socket.gethostname() 
    IP = socket.gethostbyname(host)
    print("Server Voice start...")
    print("Your Computer Name is:" + host)
    print("Your Computer IP Address is:" + IP)
    print("Your Computer Port Address is:" , port)
    server_object.bind((IP, port))
    server_object.listen()  


    #Once the client connects to the particular port, the server starts to accept the reqquest.
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
            print("Reciving voice!!")
            audio_data = np.frombuffer(audio_data,dtype=np.float32)
            input_data = np.append(input_data, audio_data)
            # print(f"The input size of data is {input_data.size}")
        
            audio_data = connection_object.recv(1024)
            
            
            if input_data.size >= audio_size:
                write('captured_audio/Recieved_audio.wav', sample_rate, input_data)  # Save as WAV file 
                print("Voice recived")
                # connection_object.close() 
                break
            
