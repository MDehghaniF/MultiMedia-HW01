import socket               # Import socket module
import cv2
import numpy as np
import time
def frame_client(port = 12345):
    client = socket.socket()         # Create a socket object
    host = socket.gethostname()     # Get local machine name
    # port = 12345                    # Reserve a port for your service.

    client.connect((host, port))
    #s.send("Hello server!")

    # captured_file = cv2.VideoCapture('Captured_video/output.avi')

    while(True):
        # ret, frame = captured_file.read()
        # if np.shape(frame) == () :
        # #if frame == None:
        #     #s.send(b"end")
        #     break
        # cv2.imwrite("frame.jpg", frame) 
        f = open("Captured_frame/frame.jpg",'rb')
        print ('Sending...')
        l = f.read(1024)
        while (l):
            print ('Sending...')
            time.sleep(0.0004)
            client.send(l)
            l = f.read(1024)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        client.send(b"end")
    client.send(b"end")
    f.close()
    print( "Done Sending")
    client.shutdown(socket.SHUT_WR)
    print (client.recv(1024))
    client.close()                # Close the socket when done

frame_client()