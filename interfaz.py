import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MainWindowHotel(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("gui/MainWindowHotel.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindowHotel()
    win.show()
    sys.exit(app.exec_())
