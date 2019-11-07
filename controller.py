from model import MainWindow, Warnings
from PyQt5 import QtWidgets


class Logic(MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui.pushButton_17.clicked.connect(self.add_zero)
        self.ui.pushButton_16.clicked.connect(self.add_one)
        self.ui.pushButton_13.clicked.connect(self.add_two)
        self.ui.pushButton_14.clicked.connect(self.add_three)
        self.ui.pushButton_5.clicked.connect(self.add_four)
        self.ui.pushButton_6.clicked.connect(self.add_five)
        self.ui.pushButton_7.clicked.connect(self.add_six)
        self.ui.pushButton_9.clicked.connect(self.add_seven)
        self.ui.pushButton_10.clicked.connect(self.add_eight)
        self.ui.pushButton_11.clicked.connect(self.add_nine)
        self.ui.pushButton_2.clicked.connect(self.clear_all)
        self.ui.pushButton_3.clicked.connect(self.correction)
        self.ui.pushButton_4.clicked.connect(self.division)
        self.ui.pushButton_12.clicked.connect(self.multiplication)
        self.ui.pushButton_8.clicked.connect(self.subtraction)
        self.ui.pushButton_15.clicked.connect(self.adding)
        self.ui.pushButton_19.clicked.connect(self.eq)
        self.ui.pushButton_18.clicked.connect(self.add_point)
        self.ui.show()

    def add_zero(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + '0')

    def add_one(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + '1')

    def add_two(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + '2')

    def add_three(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + '3')

    def add_four(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + '4')

    def add_five(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + '5')

    def add_six(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + '6')

    def add_seven(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + '7')

    def add_eight(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + '8')

    def add_nine(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + '9')

    def add_point(self):
        if self.ui.label.text() == '':
            Warnings(self)
        else:
            text = self.ui.label.text()
            self.ui.label.setText(text + '.')

    def adding(self):
        if self.ui.label.text() == '':
            Warnings(self)
        else:
            self.stack.append(self.ui.label.text())
            self.stack.append('+')
            self.ui.label.setText('')

    def subtraction(self):
        if self.ui.label.text() == '':
            Warnings(self)
        else:
            self.stack.append(self.ui.label.text())
            self.stack.append('-')
            self.ui.label.setText('')

    def division(self):
        if self.ui.label.text() == '':
            Warnings(self)
        else:
            self.stack.append(self.ui.label.text())
            self.stack.append('/')
            self.ui.label.setText('')

    def multiplication(self):
        if self.ui.label.text() == '':
            Warnings(self)
        else:
            self.stack.append(self.ui.label.text())
            self.stack.append('*')
            self.ui.label.setText('')

    def eq(self):
        self.stack.append(self.ui.label.text())
        print(self.stack)
        if len(self.stack) == 3 and self.stack[-1] != '' and self.stack[0].replace('.','',1).isdigit() and self.stack[2].replace('.','',1).isdigit():
            if self.stack[2] == '0' and self.stack[1] == '/':
                    Warnings(self)
            else:
                result = eval(self.stack[0] + self.stack[1] + self.stack[2])
                if result < 0:
                    Warnings(self)
                else:
                    self.ui.label.setText(str(result))
                    self.stack.clear()
        else:
            Warnings(self)
            self.stack.clear()

    def clear_all(self):
        self.stack.clear()
        self.ui.label.setText('')

    def correction(self):
        text = self.ui.label.text()
        self.ui.label.setText(text[:-1])
