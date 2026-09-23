"""Chạy: python main.py"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QKeySequence, QShortcut
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel,
)
from calculator import Calculator

class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.model = Calculator()
        self.setWindowTitle('Máy tính • PyQt6')
        self.setFixedSize(400, 640)
        self.setStyleSheet('background: #000; color: #f5f5f5;')
        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 24, 22, 24)
        layout.setSpacing(14)
        title = QLabel('MÁY TÍNH')
        title.setStyleSheet('color: #888; font-size: 13px;')
        layout.addWidget(title)
        layout.addStretch()
        self.hint = QLabel('')
        self.hint.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.hint.setStyleSheet('color: #aaa; font-size: 18px;')
        layout.addWidget(self.hint)
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont('Segoe UI', 32))
        self.display.setStyleSheet('border: none; padding: 8px 0;')
        self.display.setMinimumHeight(75)
        layout.addWidget(self.display)
        grid = QGridLayout()
        grid.setHorizontalSpacing(12)
        grid.setVerticalSpacing(12)
        rows = [('AC', '%', '⌫', '÷'), ('7', '8', '9', '×'),
                ('4', '5', '6', '−'), ('1', '2', '3', '+'),
                ('00', '0', '.', '=')]
        for row, keys in enumerate(rows):
            for column, key in enumerate(keys):
                button = QPushButton(key)
                button.setFixedSize(80, 80)
                button.setCursor(Qt.CursorShape.PointingHandCursor)
                color = '#f58418' if key == '=' else '#202020' if row == 0 or column == 3 else '#2e2e2e'
                button.setStyleSheet(f'''
                    QPushButton {{background: {color}; border: none;
                        border-radius: 40px; font: 26px 'Segoe UI';}}
                    QPushButton:hover {{background: #505050;}}
                    QPushButton:pressed {{background: #666;}}
                ''')
                button.clicked.connect(lambda checked=False, k=key: self.press(k))
                grid.addWidget(button, row, column)
        layout.addLayout(grid)
        shortcuts = {str(i): str(i) for i in range(10)}
        shortcuts.update({'.': '.', ',': '.', '+': '+', '-': '−', '*': '×',
                          '/': '÷', '%': '%', '=': '=', 'Return': '=',
                          'Enter': '=', 'Backspace': '⌫', 'Escape': 'AC', 'Delete': 'AC'})
        for sequence, key in shortcuts.items():
            shortcut = QShortcut(QKeySequence(sequence), self)
            shortcut.activated.connect(lambda k=key: self.press(k))

    def press(self, key):
        text = self.model.press(key)
        self.display.setText(text)
        self.display.setCursorPosition(len(text))
        self.hint.setText(f'{self.model.total} {self.model.operator}' if self.model.operator else '')
        self.display.setFont(QFont('Segoe UI', 32 if len(text) <= 14 else 20))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())
