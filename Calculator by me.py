import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.memory = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Advanced Calculator')

        # Create display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)

        # Create buttons
        self.buttons = {
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '/': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '*': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '-': (3, 3),
            '0': (4, 0), '.': (4, 1), '=': (4, 2), '+': (4, 3),
            'sin': (5, 0), 'cos': (5, 1), 'tan': (5, 2), 'log': (5, 3),
            'exp': (6, 0), 'ln': (6, 1), '(': (6, 2), ')': (6, 3),
            'sqrt': (7, 0), 'fact': (7, 1), 'C': (7, 2), 'M+': (7, 3),
            'M-': (8, 0), 'MR': (8, 1), 'MC': (8, 2)
        }

        # Create layout
        main_layout = QVBoxLayout()
        button_layout = QGridLayout()

        # Add display to layout
        main_layout.addWidget(self.display)

        # Add buttons to layout
        for btn_text, pos in self.buttons.items():
            button = QPushButton(btn_text)
            button.clicked.connect(self.onButtonClick)
            button_layout.addWidget(button, *pos)

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def onButtonClick(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = str(eval(self.parseExpression(self.display.text())))
                self.display.setText(result)
            except Exception as e:
                QMessageBox.critical(self, 'Error', 'Invalid Input', QMessageBox.Ok)
                self.display.clear()
        elif text == 'C':
            self.display.clear()
        elif text == 'M+':
            try:
                self.memory += float(eval(self.parseExpression(self.display.text())))
            except Exception as e:
                QMessageBox.critical(self, 'Error', 'Invalid Input', QMessageBox.Ok)
        elif text == 'M-':
            try:
                self.memory -= float(eval(self.parseExpression(self.display.text())))
            except Exception as e:
                QMessageBox.critical(self, 'Error', 'Invalid Input', QMessageBox.Ok)
        elif text == 'MR':
            self.display.setText(str(self.memory))
        elif text == 'MC':
            self.memory = 0
        elif text in {'sin', 'cos', 'tan', 'log', 'exp', 'ln', 'sqrt', 'fact'}:
            self.display.setText(self.display.text() + text + '(')
        else:
            self.display.setText(self.display.text() + text)

    def parseExpression(self, expression):
        # Replace function names with corresponding math module functions
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        expression = expression.replace('log', 'math.log10')
        expression = expression.replace('exp', 'math.exp')
        expression = expression.replace('ln', 'math.log')
        expression = expression.replace('sqrt', 'math.sqrt')
        expression = expression.replace('fact', 'math.factorial')
        return expression

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
