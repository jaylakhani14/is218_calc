import unittest
from src.src.CsvReader import CsvReader, ClassFactory
from src.calculator.calculator import Calculator
from pprint import pprint

class CSVTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        test_data = CsvReader('/src/csv/addition.csv').data
        self.assertEqual(calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
        self.assertEqual(calculator.result, float(row['Result']))
if __name__ == '__main__':
    unittest.main()