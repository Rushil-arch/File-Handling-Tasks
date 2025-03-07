# Task 2: Write and Append Data to a File

def write_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content + "\n")

def append_to_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content + "\n")

def read_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip())

# Taking user input and writing to 'output.txt'
user_input = input("Enter some text to write to the file: ")
write_to_file('output.txt', user_input)

# Taking additional input and appending to 'output.txt'
additional_input = input("Enter additional text to append to the file: ")
append_to_file('output.txt', additional_input)

# Reading and displaying the final content of 'output.txt'
print("Final content of the file 'output.txt':")
read_file('output.txt')


