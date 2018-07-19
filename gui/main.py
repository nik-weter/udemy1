import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from  PyQt5.Qt import *


# class Page(QWidget):
#     def __init__(self):
#         super().__init__()
#         my_label = QLabel("This is my label")
#         layout = QVBoxLayout()
#         layout.addWidget(my_label)
#
#         main_Layout = QGridLayout()
#         main_Layout.addLayout(layout, 0, 1)
#
#         self.setLayout(main_Layout)
#         self.setWindowTitle("My firt Qt App")



if __name__ == "__main__":
    import sys

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile("main.qml"))

    window = engine.rootObjects()[0]
    window.show()

    sys.exit(app.exec_())