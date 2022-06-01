import pytest
from functions_to_test import Calculator

class TestForCalculator():

    def test_add(self):
        assert Calculator.add(4, 8) == 12
        assert Calculator.add(10, 5) == 15

    def test_subtract(self):
        assert Calculator.subtract(8, 4) == 4
        assert Calculator.subtract(7, 9) == -2

    def test_multiply(self):
        assert Calculator.multiply(4, 8) == 32
        assert Calculator.multiply(7, 6) == 42

    def test_divide(self):
        assert Calculator.divide(10, 2) == 5
        with pytest.raises(ValueError) as e:
            Calculator.divide(10, 0)
        assert "Can not divide by zero!" in str(e.value)

if __name__ == '__main__':
    pytest.main()
