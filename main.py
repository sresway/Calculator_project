"""Main entry point for the calculator program (Command-Line Mode)."""

import os
import sys
import logging
from dotenv import load_dotenv
from app.app import CalculatorApp
from calculator import Calculator

# Configure logging to log both to console and a file
logging.basicConfig(
    level=logging.DEBUG,  # Change to INFO if you don't want extra debug logs
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("calculator.log"),  # Save logs to a file
        logging.StreamHandler(),  # Print logs to console
    ]
)

# Load environment variables
load_dotenv()

def format_number(n):
    """Format numbers to remove unnecessary decimals."""
    return int(n) if n == int(n) else n

def main():
    """Run the calculator in interactive mode or handle command-line arguments."""
    calc = CalculatorApp()

    # Handle command-line arguments (e.g., python main.py 5 3 add)
    if len(sys.argv) > 1:
        try:
            _, num1, num2, operation = sys.argv  
            num1, num2 = float(num1), float(num2)  
            result = calc.run_command(f"{num1} {num2} {operation}")
            print(result)
        except ValueError:
            logging.error("Invalid number input: Ensure both inputs are valid numbers.")
            print("Invalid number input: Ensure both inputs are valid numbers.")
            sys.exit(1)
        except IndexError:
            logging.error("Usage: python main.py <num1> <num2> <operation>")
            print("Usage: python main.py <num1> <num2> <operation>")
            sys.exit(1)
        return  # Exit after handling CLI arguments

    # Interactive REPL mode
    logging.info("Calculator started. Type 'exit' to quit.")
    print("Calculator started. Type 'exit' to quit.")

    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() == "exit":
                break
            print(calc.run_command(user_input))
        except KeyboardInterrupt:
            logging.warning("User interrupted program.")
            print("\nExiting calculator.")
            break
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

# Example usage of environment variable
print("Environment:", os.getenv("ENVIRONMENT"))
