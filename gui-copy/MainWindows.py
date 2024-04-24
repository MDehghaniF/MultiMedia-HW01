from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from WebcamWidget import WebcamWidget
from FillButton import FillButton
from ImageViewer import ImageViewer
import Voice as voice
import Frame as frame
from multiprocessing import Process
import time
# from Voice_cap import *

# Server function that simulates a server running
def voice_client_function(host):
    voice.TCP_transmit(host, 6666)
def frame_client_function(host):
    frame.transmit(host, 6665)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ip_value = '127.0.0.1'

        font = self.font()
        font = QFont("Times New Roman", 12)

        # Set window title and size
        self.setWindowTitle("Spyke!")
        self.setGeometry(200, 100, 1600, 900)
        self.setStyleSheet("background-color: rgb(100,100,100)")

        # Create webcam widget
        self.webcam_widget = WebcamWidget()
        self.webcam_widget.setParent(self)  # Adds it to the
        self.webcam_widget.setGeometry(880, 150, self.webcam_widget.width(), self.webcam_widget.height())  # 640 * 480

        # Create ImageViewer widget
        self.image_viewer = ImageViewer()
        self.image_viewer.setParent(self)  # Adds it to the
        self.image_viewer.setGeometry(80, 150, self.image_viewer.width(), self.image_viewer.height())  # 640 * 480

        # Create a IP label
        self.ip_label = QLabel('Enter IP Address:', self)
        self.ip_label.setGeometry(510, 35, 150, 20)
        self.ip_label.setFont(font)

        # Create a QLineEdit for entering IP address
        self.ip_line_edit = QLineEdit(self)
        self.ip_line_edit.setPlaceholderText("127.0.0.1")
        self.ip_line_edit.setGeometry(650, 35, 200, 20)
        self.ip_line_edit.setStyleSheet("background-color: lightblue; border: 2px solid darkblue;")
        self.ip_line_edit.setFont(font)

        # Create a Button for connecting
        self.connect_button = QPushButton('Disconnected', self)
        self.connect_button.setGeometry(860, 25, 130, 40)  # Set button position and size
        self.connect_button.clicked.connect(self.connect_button_clicked)  # Connect button click event to a function
        self.connect_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(255,0,0);
                border: 2px solid darkred;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: rgb(255,100,100);
            }
        """)
        self.connect_button.setFont(font)

        # Create a Button for Sending
        self.send_button = QPushButton('Send', self)
        self.send_button.setGeometry(1125, 800, 150, 50)  # Set button position and size
        self.send_button.clicked.connect(self.send_button_clicked)  # Connect button click event to a function
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: lightblue;
                border: 2px solid darkblue;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: rgb(100,100,200);
            }
        """)
        self.send_button.setFont(font)

        # Create a button for Recording
        self.record_button = FillButton("Record", self)
        self.record_button.setGeometry(950, 650, 180, 50)
        self.record_button.setFont(font)
        self.record_button.clicked.connect(self.record_button_clicked)

        # Create a button for capturing an image
        self.capture_button = QPushButton('Capture', self)
        self.capture_button.setGeometry(1260, 650, 180, 50)  # Set button position and size
        self.capture_button.clicked.connect(self.capture_button_clicked)  # Connect button click event to a function
        self.capture_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(255,0,0);
                border: 2px solid darkred;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: rgb(255,100,100);
            }
        """)
        self.capture_button.setFont(font)

        # Create a button for showing the image
        self.show_button = QPushButton('Show', self)
        self.show_button.setGeometry(460, 650, 180, 50)  # Set button position and size
        self.show_button.clicked.connect(self.show_button_clicked)  # Connect button click event to a function
        self.show_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(255,0,0);
                border: 2px solid darkred;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: rgb(255,100,100);
            }
        """)
        self.show_button.setFont(font)

        # Create a button for playing
        self.play_button = FillButton("Play", self)
        self.play_button.setGeometry(150, 650, 180, 50)
        self.play_button.setFont(font)
        self.play_button.clicked.connect(self.play_button_clicked)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.cyan, 1, Qt.SolidLine))  # Pen color, width, and style
        painter.drawLine(800, 100, 800, 800)

    def send_button_clicked(self):
        self.send_button.setText("Sent")
        # Create a separate process for the server function
        try:
            server_process = Process(target=frame_client_function, args=(self.ip_value,))
            server_process.start()
            time.sleep(6)
            server_process.join()  # Wait for the process to finish
        except ConnectionRefusedError as e:
            QMessageBox.critical(self, "Error", "Can not find the server!! Check your IP again")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
        try:
            server_process = Process(target=voice_client_function, args=(self.ip_value,))
            server_process.start()
            time.sleep(6)
            server_process.join()  # Wait for the process to finish
        except ConnectionRefusedError as e:
            QMessageBox.critical(self, "Error", "Can not find the server!! Check your IP again")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")


    def connect_button_clicked(self):
        self.connect_button.setText("Connected")
        self.connect_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(0,255,0);
                border: 2px solid darkgreen;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: rgb(100,255,100);
            }
        """)
        self.ip_value = self.ip_line_edit.text()
        print("Recived IP is : ", self.ip_value)
        # voice.voice_server()


    def capture_button_clicked(self):
        self.webcam_widget.capture_frame()
        # capture an image from the webcam

    def show_button_clicked(self):
        self.image_viewer.show_frame()
        # frame.display()

    def play_button_clicked(self):
        self.play_button.setText("Playing")
        # print(self.ip_value)
        voice.play()

    def record_button_clicked(self):
        self.record_button.setText("Recording")
        voice.record()

