# task2_greeting.py

# Taking user's first and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Creating full name
full_name = first_name.strip().title() + " " + last_name.strip().title()

# Displaying personalized greeting
print(f"\nHello, {full_name}! Welcome to Python programming!")
