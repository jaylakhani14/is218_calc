import unittest

from src.calculator import Calculator
from src.CsvReader.CsvReader import CsvReader
from pprint import pprint

class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader("../tests/csv/addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        test_data = CsvReader("../tests/csv/subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CsvReader("../tests/csv/multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.mult(row['Value 1'], row['Value 2']), result)

    def test_division(self):
        test_data = CsvReader("../tests/csv/division.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divi(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square(self):
        test_data = CsvReader("../tests/csv/square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.squ(row['Value 1']), result)

    def test_square_root(self):
        test_data = CsvReader("../tests/csv/squareRoot.csv").data
        for row in test_data:
            result = round(float(row['Result']), 8)
            self.assertEqual(self.calculator.root(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.divi(0, 0))

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()
