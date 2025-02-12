class Calculator:
    _history = []

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculator._history.append(f"{a} + {b} = {result}")
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculator._history.append(f"{a} - {b} = {result}")
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculator._history.append(f"{a} * {b} = {result}")
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = a / b
        Calculator._history.append(f"{a} / {b} = {result}")
        return result

    @classmethod
    def get_history(cls):
        return cls._history

    @classmethod
    def clear_history(cls):
        cls._history.clear()
