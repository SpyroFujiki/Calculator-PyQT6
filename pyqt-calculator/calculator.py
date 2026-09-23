"""Bộ tính độc lập với giao diện; phép tính thực hiện từ trái sang phải."""
from decimal import Decimal, localcontext


class Calculator:
    def __init__(self):
        self.clear()

    def clear(self):
        self.entry = '0'
        self.total = None
        self.operator = None
        self.new_entry = True
        self.error = False

    def press(self, key):
        if key == 'AC':
            self.clear()
            return self.entry
        if self.error:
            self.clear()
        try:
            with localcontext() as context:
                context.prec = 28
                self._handle(key)
        except (ArithmeticError, ValueError):
            self.clear()
            self.entry = 'Lỗi: chia cho 0'
            self.error = True
        return self.entry

    def _handle(self, key):
        if key in ('00', '.') or (len(key) == 1 and key.isdigit()):
            if self.new_entry:
                self.entry = '0'
                self.new_entry = False
            if key == '.':
                if '.' not in self.entry:
                    self.entry += '.'
            elif len(self.entry.replace('.', '').lstrip('-')) < 16:
                self.entry = (self.entry + key) if self.entry != '0' else (key.lstrip('0') or '0')
        elif key == '⌫':
            if not self.new_entry:
                self.entry = self.entry[:-1]
                if self.entry in ('', '-'):
                    self.entry = '0'
        elif key == '%':
            self.entry = self.format(Decimal(self.entry) / 100)
        elif key in ('+', '−', '×', '÷', '='):
            value = Decimal(self.entry)
            if self.operator and not self.new_entry:
                value = self.calculate(self.total, value, self.operator)
                self.entry = self.format(value)
            self.total = value
            self.operator = None if key == '=' else key
            self.new_entry = True

    @staticmethod
    def calculate(a, b, operator):
        if operator == '+':
            return a + b
        if operator == '−':
            return a - b
        if operator == '×':
            return a * b
        return a / b

    @staticmethod
    def format(value):
        if value == 0:
            return '0'
        text = format(value, 'f')
        return text.rstrip('0').rstrip('.') if '.' in text else text
