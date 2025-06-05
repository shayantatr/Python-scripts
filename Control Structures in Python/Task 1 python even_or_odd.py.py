# Task 1: Check if a Number is Even or Odd

# 1. Takes an integer input from the user.

numbers = int(input("Enter an Integer Number: "))


# 2. Checks whether the number is even or odd using an if-else statement.

if numbers % 2 == 0:
    print(f"The number {numbers} is Even")
else:
    print(f"The number {numbers} is Odd")
print("Thank You")
