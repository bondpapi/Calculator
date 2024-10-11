class Calculator:
    def __init__(self):
        self.memory = 0.0

    def add(self, numb: float) -> float:
        """Add number to memory."""
        self.memory += numb
        return self.memory

    def subtract(self, numb: float) -> float:
        """Subtract number from memory."""
        self.memory -= numb
        return self.memory

    def multiply(self, numb: float) -> float:
        """Multiplies a number to memory."""
        self.memory *= numb
        return self.memory

    def divide(self, numb: float) -> float:
        """Divides the memory by a number."""
        if numb == 0:
            raise ValueError("Cannot Divide by Zero")
        self.memory /= numb
        return self.memory

    def root(self, n: int) -> float:
        """Take the Nth root of the number in memory."""
        if n == 0:
            raise ValueError("Cannot calculate 0th root")
        if self.memory < 0 and n % 2 == 0:
            raise ValueError("Cannot take the root of a negative number.")
        self.memory **= 1 / n
        return self.memory

    def reset(self) -> None:
        """Reset the memory to zero."""
        self.memory = 0.0
