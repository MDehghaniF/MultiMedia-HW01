from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class FillButton(QPushButton):
    def __init__(self, label, parent=None):
        super().__init__(parent)
        # Initial properties
        self.fill_portion = 0
        self.label = label
        self.animation_timer = QTimer(self)
        self.timer = QTimer(self)
        self.animation_timer.timeout.connect(self.fill_update)
        self.setStyleSheet("""
        QPushButton {
            background-color: rgb(255,0,0);
            border: 2px solid darkred;
            border-radius: 25px;
        }
        QPushButton:hover {
            background-color: rgb(255,100,100);
        }
        """)
        self.setText(label)
        self.clicked.connect(self.fill_button_clicked)

    def fill_button_clicked(self):
        self.setStyleSheet("""
        QPushButton {
            background-color: rgb(100,100,100);
            border: 2px solid darkred;
            border-radius: 25px;
        }
        """)

        if self.fill_portion == 0 or self.fill_portion == 1000:
            self.fill_portion = 0
            self.animation_timer.start(3)
            # self.timer.start(1000)

    def fill_update(self):
        if self.fill_portion < 1000:
            self.fill_portion += 1
            self.setStyleSheet("""
            QPushButton
            {{background-color: qlineargradient(spread:pad, x1: 0, y1: 0, x2: 1, y2: 0, stop:0 rgb(255,0,0), stop: {} rgb(100,100,100));
            border: 2px solid darkred;
            border-radius: 25px;
            }}
            """.format(self.fill_portion/1000))
        else:
            self.animation_timer.stop()
            self.setText(self.label)
            self.setStyleSheet("""
                    QPushButton {
                        background-color: rgb(255,0,0);
                        border: 2px solid darkred;
                        border-radius: 25px;
                    }
                    QPushButton:hover {
                        background-color: rgb(255,100,100);
                    }
                    """)
