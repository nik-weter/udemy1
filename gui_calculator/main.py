import os, sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Button:
    def __init__(self, text, result):
        self.b = QPushButton(str(text))
        self.text = text
        self.result = result
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, v):
        if v == "=":
            res = eval(self.result.text())
            self.result.setText(str(res))
        elif v == "AC":
            res = ""
            self.result.setText(res)
        elif v == "√":
            res = math.sqrt(float(self.result.text()))
            self.result.setText(str(res))
        elif v == "DEL":
            res = self.result.text()
            res = res[:-1]
            self.result.setText(str(res))
        else:
            current_value = self.result.text()
            new_value = current_value + str(v)
            self.result.setText(new_value)
        print("clicked ", v)

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.createapp()

    def createapp(self):
        #Create our grid
        grid = QGridLayout()
        result = QLineEdit()
        grid.addWidget(result, 0, 0, 1, 4)

        buttons = ["AC", "√", "DEL", "/",
                   7, 8, 9, "*",
                   4, 5, 6, "-",
                   1, 2, 3, "+",
                   0, ".", "="
                   ]
        row = 1
        cow = 0



        for button in buttons:
            if cow > 3:
                row += 1
                cow = 0
            buttonObject = Button(button, result)

            if button == "=":
                grid.addWidget(buttonObject.b, row, cow, 1, 2)
                cow += 1
            else:
                grid.addWidget(buttonObject.b, row, cow, 1, 1)
            cow += 1

        self.setLayout(grid)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())