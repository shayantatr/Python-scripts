# write_append_file.py

file_name = "output.txt"

# Step 1: Take user input and write to the file
user_input = input("Enter text to write to the file: ")
with open(file_name, "w") as file:
    file.write(user_input + "\n")
    print("Data successfully write to output.text.","\n")

# Step 2: Append additional data
additional_data = input("Enter additional text to append: ")
with open(file_name, "a") as file:
    file.write(additional_data + "\n")
    print("Data successfully appended.")

# Step 3: Read and display final content
print("\nFinal content of file output.txt:")
with open(file_name, "r") as file:
    for line in file:
        print(line.strip())
