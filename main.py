"""Main entry point for the calculator program."""

import sys
from calculator import Calculator

def format_number(n):
    """Format numbers to remove unnecessary decimals."""
    return int(n) if n == int(n) else n

def main():
    """Main function to handle user input for the calculator."""
    if len(sys.argv) != 4:
        print("Usage: python main.py <num1> <num2> <operation>")
        sys.exit(1)

    num1, num2, operation = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print(f"Invalid number input: {num1} or {num2} is not a valid number.")
        sys.exit(1)

    calculator = Calculator()
    result = None

    if operation == "add":
        result = calculator.add(num1, num2)
    elif operation == "subtract":
        result = calculator.subtract(num1, num2)
    elif operation == "multiply":
        result = calculator.multiply(num1, num2)
    elif operation == "divide":
        try:
            result = calculator.divide(num1, num2)
        except ValueError:
            print("An error occurred: Cannot divide by zero")
            sys.exit(1)
    else:
        print(f"Unknown operation: {operation}")
        sys.exit(1)

    # ✅ Fixed the f-string syntax error
    print(
        f"The result of {format_number(num1)} {operation} "
        f"{format_number(num2)} is equal to {format_number(result)}"
    )


if __name__ == "__main__":
    main()
