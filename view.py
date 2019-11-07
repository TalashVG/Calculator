from controller import Logic
from PyQt5 import QtWidgets
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Logic()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
