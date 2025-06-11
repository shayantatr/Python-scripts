# Task 1: Create a Dictionary of Student Marks.

# 1. Creates a dictionary where student names are keys and their marks are values.

student_marks = {"Alice":85,"Bob":92,"Charlie":78,"Diana":88,"Ethan":95}

# 2.  Asks the user to input a student's name.

student_name = input("Enter the Student's Name : ")

# (3.   Retrieves and displays the corresponding marks. 4. If the student’s name is not found, display an appropriate message.)

if student_name in student_marks:
    print(f"{student_name}'s marks : {student_marks[student_name]}")
else:
    print("Student not found in the records.")