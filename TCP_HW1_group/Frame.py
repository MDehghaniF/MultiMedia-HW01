import socket
import numpy as np
from multiprocessing import Process
import time
import cv2

def transmit(ip_address = '127.0.0.1', port = 5553):

    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)    # Create a socket object
    host = socket.gethostname() # Get local machine name
    # port = 12345                 # Reserve a port for your service.

    client.connect((ip_address, port))

        
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
        break    # Close the socket when done


def server(port = 6665):
        


    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    IP = socket.gethostbyname(host)
    print("Server Frame start...")
    print("Your Computer Name is:" + host)
    print("Your Computer IP Address is:" + IP)
    print("Your Computer Port Address is:" , port)
    s.bind((IP, port))         # Bind to the port
    s.listen(5)                # Now wait for client connection.

    while True:
        c, addr = s.accept()  # Establish connection with client.
        with open('./Frames/torecv.jpg', 'wb') as f:
            print('Got connection from', addr)
            print("Receiving...")
            while True:
                l = c.recv(1024)
                if not l:         
                    break
                f.write(l)
        print("Done Receiving")
        c.close()  # Close the connection
                
def display():
    img = cv2.imread('./Frames/torecv.jpg', cv2.IMREAD_COLOR)

    # Display the image in a window
    cv2.imshow('Image Window', img)

    # Wait for any key to be pressed before closing the window
    cv2.waitKey(0)
    # cv2.close
    