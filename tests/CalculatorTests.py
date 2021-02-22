import unittest

from src.calculator.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader("../tests/Data/Unit Test addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtract_method_calculator(self):
        test_data = CsvReader("../tests/Data/Unit Test subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculator(self):
        test_data = CsvReader("../tests/Data/Unit Test multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.mult(row['Value 1'], row['Value 2']), result)

    def test_divide_method_calculator(self):
        test_data = CsvReader("../tests/Data/Unit division.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divi(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_method_calculator(self):
        test_data = CsvReader("../tests/Data/Unit Test square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.squ(row['Value 1']), result)


def test_square_root_method_calculator(self):
        test_data = CsvReader("../tests/Data/Unit Test squareRoot.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.root(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == "__main__":
    unittest.main()
