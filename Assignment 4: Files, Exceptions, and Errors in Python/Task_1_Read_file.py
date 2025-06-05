# Task 1: Read a File and Handle Errors

# 1.  Opens and reads a text file named sample.txt.

try:
    file = open('Sample.txt','r')

# 2.  Prints its content line by line.

    print('Readding file content:')

# 3.  Handles errors gracefully if the file does not exist.

    for line in file:
        print(line.strip())
    
except FileNotFoundError:
    print("Error: The file 'Sample.txt' was not found")

file.close()


