# Writing to a file
filename = "sample.txt"

# Take input from the user
text_to_write = input("Enter some text to write to the file: ")

# Open the file in write mode ('w') and write the input
with open(filename, 'w') as write_file:
    write_file.write(text_to_write + '\n')
    print("Data written to the file successfully.")

# Reading from the file
try:
    with open(filename, 'r') as read_file:
        print("Reading from the file:")
        for line in read_file:
            print(line.strip())  # Display each line without trailing newlines
except FileNotFoundError:
    print(f"Error: {filename} not found.")
