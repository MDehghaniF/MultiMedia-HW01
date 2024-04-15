import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2


class WebcamWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Open webcam
        self.cap = cv2.VideoCapture(0)

        # Create label to display video feed
        self.video_label = QLabel()
        self.video_label.setAlignment(Qt.AlignCenter)
        self.setVisible(True)
        #
        # # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        self.setLayout(layout)

        # Create a timer to update the video feed
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(25)  # Update every 25 milliseconds

        # A flag used for capturing the video
        self.capture_flag = False

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            if self.capture_flag:
                cv2.imwrite("Frames/frame.jpg", frame)
                self.capture_flag = False
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.video_label.setPixmap(pixmap)

    def capture_frame(self):
        self.capture_flag = True
