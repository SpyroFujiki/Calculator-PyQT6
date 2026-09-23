import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):
    def run_keys(self, keys):
        model = Calculator()
        for key in keys:
            model.press(key)
        return model

    def test_arithmetic(self):
        for keys, expected in [('12+3=', '15'), ('9−4=', '5'), ('6×7=', '42'),
                               ('8÷2=', '4'), ('0.1+0.2=', '0.3'), ('2+3×4=', '20')]:
            with self.subTest(keys=keys):
                self.assertEqual(self.run_keys(keys).entry, expected)

    def test_percent_and_edit(self):
        self.assertEqual(self.run_keys('50%').entry, '0.5')
        self.assertEqual(self.run_keys('123⌫').entry, '12')
        self.assertEqual(self.run_keys('2+×3=').entry, '6')

    def test_error_recovery_and_new_input(self):
        self.assertTrue(self.run_keys('1÷0=').error)
        self.assertEqual(self.run_keys('1÷0=7').entry, '7')
        self.assertEqual(self.run_keys('2+3=9').entry, '9')

if __name__ == '__main__':
    unittest.main()
