# Calculator

This Python package provides a simple calculator class for performing basic arithmetic operations. It also has a memory reset

## Installation
To install the calculator package, follow these steps:

1. Clone the repository:

git clone https://github.com/bondpapi/calculator

2. Navigate into the project directory:

cd calculator

3. Install the package:

pip install .


Alternatively, if the package is published on PyPI, you can install it directly with:

pip install calculator

Once installed, you can use the Calculator class in your Python code as follows:

from calculator import Calculator

# Create a calculator instance
calc = Calculator()

# Perform some operations
print(calc.add(10))          #Adds 10 to memory, returns 10

print(calc.subtract(3))      #Subtracts 3 from memory, returns 7

print(calc.multiply(2))      #Multiplies memory by 2, returns 14

print(calc.divide(4))        #Divides memory by 4, returns 3.5

print(calc.root(2))          #Takes the square root of memory, returns ~1.87

calc.reset()                 #Resets memory to 0

print(calc.memory)           #Should print 0



You can run the provided tests using pytest. Make sure pytest is installed, and from the project directory, run:

pytest
