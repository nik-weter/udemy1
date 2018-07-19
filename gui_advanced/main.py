import sys, os
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.label = QLabel("Name")
        self.input_label = QLabel("Please, input your name.")
        self.name_input = QLineEdit()
        self.button = QPushButton("Set name")
        self.button.pressed.connect(self.pressButton)
        self.button.released.connect(self.releaseButton)

        h = QHBoxLayout()

        h.addWidget(self.label)
        h.addWidget(self.name_input)

        v = QVBoxLayout()
        v.addWidget(self.input_label)
        v.addLayout(h)
        v.addWidget(self.button)
        self.setLayout(v)

        self.setWindowTitle("Horyzontal Layout")
        self.show()

    def pressButton(self):
        print("Button is being pressed ")
        input_text = self.name_input.text()
        self.input_label.setText("You input " + input_text)
        self.setWindowTitle(input_text + "'s window")

    def releaseButton(self):
        print("Button has been released")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
