# Task 2: Using the Math Module for Calculations

# import Library

import math

# 1.  Asks the user for a number as input.

try:

    number = float(input("Enter a Number : "))

# 2. Uses the math module to calculate the:
# 3. Displays the calculated results.

    if number <= 0:
        print("Logarithm is only defined for positive numbers.")

    else:

        # Square root of the number
        print(f"Square root of {number} : {math.sqrt(number)}")

        # Natural logarithm (log base e) of the number
        print(f"Natural logarithm of {number} : {math.log(number)}")

        # Sine of the number (in radians)
        print(f"Sine of {number} : {math.sin(number)}")

except ValueError:
    print("Invalid input. Please enter a numeric value.")
