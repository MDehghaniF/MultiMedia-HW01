import os
from MainWindows import MainWindow
import sys
import Voice as voice
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
from multiprocessing import Process
import time

# Server function that simulates a server running
def server_function():
    voice.voice_server()

if __name__ == "__main__":
    # Create a separate process for the server function
    server_process = Process(target=server_function)
    server_process.start()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

