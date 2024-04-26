import os
from MainWindows import MainWindow
import sys
import Voice as voice
import Frame as frame
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
from multiprocessing import Process
import time

# Server function that simulates a server running
def voice_server_function():
    voice.voice_server()
def frame_server_function():
    frame.server()

if __name__ == "__main__":
    # Create a separate process for the server function
    voice_server_process = Process(target=voice_server_function)
    voice_server_process.start()
    
    frame_server_process = Process(target=frame_server_function)
    frame_server_process.start()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

