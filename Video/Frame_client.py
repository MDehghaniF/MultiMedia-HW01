import socket               # Import socket module
import cv2
import numpy as np
import time
def frame_client(port = 12345):
    client = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 12345                 # Reserve a port for your service.

    client.connect((host, port))


    # while(True):
    #     f = open("Frames/frame.jpg",'rb')
    #     # print ('Sending...')
    #     l = f.read(1024)
    #     while (l):
    #         print ('Sending...')
    #         time.sleep(0.0004)
    #         client.send(l)

    #         l = f.read(1024)
    # #     if cv2.waitKey(1) & 0xFF == ord('q'): 
    # #         break
    #     client.send(b"end")
    # client.send(b"end")
    # f.close()
    # print("Done Sending")
    # client.shutdown(socket.SHUT_WR)
    # print (client.recv(1024))

    while True:
        with open("Frames/frame.jpg", 'rb') as f:
            while True:
                l = f.read(1024)
                if not l:
                    print("FINISHING!!!!")
                    # client.shutdown(socket.SHUT_WR)
                    break
                else:
                    print('Sending...')
                    time.sleep(0.0004)
                    client.send(l)
            # client.shutdown(socket.SHUT_WR)
        break

frame_client()