from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(380, 500)
        self.show()
        self.setStyleSheet('background:black; font-size:30px;')
        main_layout = QVBoxLayout()
        button_layout = QGridLayout()

        
        
        self.entrybox = QLineEdit()
        self.entrybox.setFixedSize(350, 60)
        self.entrybox.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.entrybox.setStyleSheet('color:white;')
        
        main_layout.addWidget(self.entrybox)

        button0 = QPushButton(text='0', clicked=lambda:self.insertNum('0'))
        button00 = QPushButton(text='00', clicked=lambda:self.insertNum('00'))
        button1 = QPushButton(text='1', clicked=lambda:self.insertNum('1'))
        button2 = QPushButton(text='2', clicked=lambda:self.insertNum('2'))
        button3 = QPushButton(text='3', clicked=lambda:self.insertNum('3'))
        button4 = QPushButton(text='4', clicked=lambda:self.insertNum('4'))
        button5 = QPushButton(text='5', clicked=lambda:self.insertNum('5'))
        button6 = QPushButton(text='6', clicked=lambda:self.insertNum('6'))
        button7 = QPushButton(text='7', clicked=lambda:self.insertNum('7'))
        button8 = QPushButton(text='8', clicked=lambda:self.insertNum('8'))
        button9 = QPushButton(text='9', clicked=lambda:self.insertNum('9'))

        button_dot = QPushButton(text='.', clicked=lambda:self.insertNum('.'))
        button_back = QPushButton(text='⌫', clicked=self.eraseItem)
        button_mod = QPushButton(text='%', clicked=lambda:self.insertNum('%'))
        button_reset = QPushButton(text='AC', clicked=self.clearItems)

        button_add = QPushButton(text='+', clicked=lambda:self.insertNum('+'))
        button_sub = QPushButton(text='-', clicked=lambda:self.insertNum('-'))
        button_mult = QPushButton(text='×', clicked=lambda:self.insertNum('×'))
        button_div = QPushButton(text='÷', clicked=lambda:self.insertNum('÷'))
        button_calculate = QPushButton(text='=', clicked=self.calculate)


        buttons = [
            button0, button00, button1, button2, button3,
            button4, button5, button6, button7, button8, button9,
            button_dot, button_back, button_mod, button_reset,
            button_add, button_sub, button_mult, button_div, button_calculate
        ]

        for button in buttons:
            button.setFixedSize(80, 80)
            

        buttons_digit = [
            button0, button00, button1, button2, button3,
            button4, button5, button6, button7, button8, button9,
            button_dot
        ]   

        for button in buttons_digit:
            button.setStyleSheet('background: #1E1E1E; border-radius: 40px;')

        
        buttons_symbol = [
            button_back, button_mod, button_reset,
            button_add, button_sub, button_mult, button_div
        ]

        for button in buttons_symbol:
            button.setStyleSheet('background: #282626; border-radius: 40px;')

        button_calculate.setStyleSheet('background:#FF8500; border-radius: 40px;')

        button_layout.addWidget(button_reset, 0, 0)
        button_layout.addWidget(button_mod, 0, 1)
        button_layout.addWidget(button_back, 0, 2)
        button_layout.addWidget(button_div, 0, 3)
        button_layout.addWidget(button7, 1, 0)
        button_layout.addWidget(button8, 1, 1)
        button_layout.addWidget(button9, 1, 2)
        button_layout.addWidget(button_mult, 1, 3)
        button_layout.addWidget(button4, 2, 0)
        button_layout.addWidget(button5, 2, 1)
        button_layout.addWidget(button6, 2, 2)
        button_layout.addWidget(button_sub, 2, 3)
        button_layout.addWidget(button1, 3, 0)
        button_layout.addWidget(button2, 3, 1)
        button_layout.addWidget(button3, 3, 2)
        button_layout.addWidget(button_add, 3, 3)
        button_layout.addWidget(button00, 4, 0)
        button_layout.addWidget(button0, 4, 1)
        button_layout.addWidget(button_dot, 4, 2)
        button_layout.addWidget(button_calculate, 4, 3)


        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def insertNum(self, num):
        expression = self.entrybox.text()
        self.entrybox.setText('')
        if expression == 'ERROR':
            expression = ''
        expression += num

        self.entrybox.setText(expression)

    def clearItems(self):
        self.entrybox.clear()

    def eraseItem(self):
        self.entrybox.backspace()

    def calculate(self):
        items_to_calculate = self.entrybox.text()

        try:
            if items_to_calculate:
                expression = items_to_calculate.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                self.entrybox.setText(str(result))
        except:
            self.entrybox.setText('ERROR')


app = QApplication([])
app.setStyle('fusion')
main = Main()
app.exec()
