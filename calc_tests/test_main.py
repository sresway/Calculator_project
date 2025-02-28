"""Test suite for the main calculator program."""

import subprocess
import pytest

@pytest.mark.parametrize(
    "args, expected",
    [
        (["5", "3", "add"], "The result of 5 add 3 is equal to 8"),
        (["10", "2", "subtract"], "The result of 10 subtract 2 is equal to 8"),
        (["4", "5", "multiply"], "The result of 4 multiply 5 is equal to 20"),
        (["20", "4", "divide"], "The result of 20 divide 4 is equal to 5"),
        (["1", "0", "divide"], "An error occurred: Division by zero is not allowed"),
        (["9", "3", "unknown"], "Unknown operation: unknown"),
        (["a", "3", "add"], "Invalid number input: Ensure both inputs are valid numbers."),
        (["5", "b", "subtract"], "Invalid number input: Ensure both inputs are valid numbers."),
    ]
)
def test_main(args, expected):
    """Test command-line input for the calculator program."""
    result = subprocess.run(
        ["python", "main.py"] + args, capture_output=True, text=True, check=False
    )
    assert expected in result.stdout or expected.replace("5.0", "5") in result.stdout
