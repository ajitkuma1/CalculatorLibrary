""" Unit test for calculator functions"""
import calculator


class TestCalculator:
    def test_addtion(self):
        assert 5 == calculator.addNumbers(2, 3)

    def test_subtraction(self):
        assert -4 == calculator.subtractNumber(1, 5)

    def test_multiplication(self):
        assert 100 == calculator.multiplyNumbers(10, 10)
