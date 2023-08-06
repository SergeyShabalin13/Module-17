import pytest
from app.calc import Calculator

class TestCalc:
    def  setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 4, 2) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(self, 3, 2) == 6

    def test_division_success(self):
        assert self.calc.division(self, 6, 2) == 3
