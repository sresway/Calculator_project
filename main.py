"""Main entry point for the calculator program (Command-Line Mode)."""

import sys
from calculator import Calculator
from app.app import CalculatorApp

def main():
    """Run the calculator as a command-line tool."""
    calc = CalculatorApp()
    
    if len(sys.argv) > 1:
        command = " ".join(sys.argv[1:])
        print(calc.run_command(command))
        return

    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break
        print(calc.run_command(user_input))

if __name__ == "__main__":
    main()

def format_number(n):
    """Format numbers to remove unnecessary decimals."""
    return int(n) if n == int(n) else n

def main():
    """Handle command-line arguments and perform calculations."""
    try:
        _, num1, num2, operation = sys.argv 
        num1, num2 = float(num1), float(num2)  
        calculator = Calculator()

        try:
            result = getattr(calculator, operation)(num1, num2)  
            print(
                f"The result of {format_number(num1)} {operation} "
                f"{format_number(num2)} is equal to {format_number(result)}"
            )
        except AttributeError:
            print(f"Unknown operation: {operation}")
            sys.exit(1)
        except ValueError as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

    except ValueError:
        print("Invalid number input: Ensure both inputs are valid numbers.")
        sys.exit(1)
    except IndexError:
        print("Usage: python main.py <num1> <num2> <operation>")
        sys.exit(1)
        