# Task 1: Calculate Factorial Using a Function.

# 1. Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.

def factorial(n):
    """Calculate factorial using a loop."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
# 2. Returns the calculated factorial.

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 3. Calls the function with a sample number and prints the output.

number = int(input("Enter a Number"))
print(f"The factorial of {number} is: {factorial(number)}")
