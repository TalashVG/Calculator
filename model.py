from PyQt5 import QtWidgets, uic, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self.stack = []
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = uic.loadUi('Calculator.ui')
        self.ui.setWindowTitle('Calculator')
        self.ui.setWindowIcon(QtGui.QIcon('Calculator.ico'))


class Warnings(QtWidgets.QMessageBox):
    def __init__(self, parent=None):
        QtWidgets.QMessageBox.__init__(self, parent)
        self.setIcon(QtWidgets.QMessageBox.Warning)
        self.setWindowIcon(QtGui.QIcon('Calculator.ico'))
        self.setText("Warning")
        self.setInformativeText("Invalid value")
        self.setWindowTitle("Warning")
        self.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.show()
