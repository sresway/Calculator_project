"""Calculator Application Module"""

from commands import add, subtract, multiply, divide

class CalculatorApp:
    """Main calculator application."""

    def __init__(self):
        """Initialize the calculator with available commands."""
        self.commands = {
            "add": add.execute,
            "subtract": subtract.execute,
            "multiply": multiply.execute,
            "divide": divide.execute,
        }

    def run_command(self, command_str):
        """Execute a command if valid. If not, return an error message."""
        try:
            if command_str.lower() == "menu":
                return "Available Commands: add, subtract, multiply, divide"

            parts = command_str.split()
            if len(parts) != 3:
                return "Invalid command format. Use: <num1> <num2> <operation>"

            num1, num2, operation = parts
            try:
                num1, num2 = float(num1), float(num2)
            except ValueError:
                return "Invalid number input: Ensure both inputs are valid numbers."

            if operation not in self.commands:
                return f"Unknown operation: {operation}"

            result = self.commands[operation](num1, num2)
            return f"Result: {result}"

        except ZeroDivisionError:
            return "An error occurred: Division by zero is not allowed"

        except KeyError:
            return f"Unknown operation: {operation}"
        