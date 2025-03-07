# Task 1: Read a File and Handle Errors

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

# Calling the function with the file name 'sample.txt'
read_file('sample.txt')


