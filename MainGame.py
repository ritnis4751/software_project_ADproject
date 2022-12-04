from GameWindow import GameWindow
from PyQt5.QtWidgets import QApplication
import sys


class WindowMaker:
    def __init__(self):
        self.window = GameWindow()
        self.window.close()

    def show_window(self):
        self.window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windowMaker = WindowMaker()
    windowMaker.show_window()
    sys.exit(app.exec_())
