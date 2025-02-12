"""Testing for the Calculator class."""

import pytest
from calculator import Calculator

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (2.5, 3.5, 6.0),
        (-2.5, 3.5, 1.0),
    ]
)
def test_addition(a, b, expected):
    """Test the addition operation."""
    result = Calculator.add(a, b)
    assert result == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (0, 0, 0),
        (-5, -3, -2),
        (10.5, 5.5, 5.0),
        (-10.5, -5.5, -5.0),
    ]
)
def test_subtraction(a, b, expected):
    """Test the subtraction operation."""
    result = Calculator.subtract(a, b)
    assert result == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (0, 10, 0),
        (-2, -3, 6),
        (2.5, 4.0, 10.0),
        (-2.5, 4.0, -10.0),
    ]
)
def test_multiplication(a, b, expected):
    """Test multiplication operation."""
    result = Calculator.multiply(a, b)
    assert result == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),
        (-6, -3, 2.0),
        (6.0, 3.0, 2.0),
        (-6.0, 3.0, -2.0),
        (0, 5, 0.0),
    ]
)
def test_division(a, b, expected):
    """Test division method."""
    result = Calculator.divide(a, b)
    assert result == expected

@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),
        (-1, 0),
        (0, 0),
    ]
)
def test_division_by_zero(a, b):
    """Test division method by 0 """
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        Calculator.divide(a, b)

@pytest.mark.parametrize(
    "operations, expected",
    [
        (["add 5 3", "subtract 10 4", "multiply 6 7", "divide 8 2"], True),
        (["history"], True),
    ]
)
def test_history(operations, expected, monkeypatch):
    """Test the history function."""
    input_iterator = iter(operations + ["exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    calc = Calculator()
    assert (len(calc.get_history()) > 0) == expected
