import socket               # Import socket module
import cv2
import numpy as np
import time

def frame_server():
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 12345                 # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter('server_output.avi', fourcc, 20.0, (640,  480))

    s.listen(5)                 # Now wait for client connection.
    f = open('Frames/receivedFrame.png','wb')
    while True:
        
        
        c, addr = s.accept()     # Establish connection with client.
        print( 'Got connection from', addr)
        print ("Receiving...")
        l = c.recv(1024)
        while (l):
            if (l == b"end"):
                # frame = cv2.imread('torecv.png')
                # print("Frame: ",frame)
                # out.write(frame)
                time.sleep(0.0004)
                l = c.recv(1024)
                f.close()
                break
            else:
                print( "Receiving...")
                f.write(l)
                l = c.recv(1024)


        # f.close()
        # out.release()
        print( "Done Receiving")
        #c.send('Thank you for connecting')
        c.close()    # Close the connection
                    

frame_server()