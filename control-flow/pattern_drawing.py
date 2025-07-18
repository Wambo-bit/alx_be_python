# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for each row
while row < size:
    # For loop for each column
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after a row is printed
    row += 1
