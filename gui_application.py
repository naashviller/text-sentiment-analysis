from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from Gui import view

import time


def run():

    app = QApplication([])
    win = view.StartWindow()
    win.setWindowTitle('Camera Calibration Application')

    win.resize(1500, 1000)
    win.show()
    app.exit(app.exec_())

run()