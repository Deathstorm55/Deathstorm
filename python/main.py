#Program Counter that increases dynamically to the absolute number of your class

# Define class size
class_size = int(input("Enter your class size: "))

# Initialize program counter
program_counter = 0

# Print initial program counter value
print("Initial Program Counter:", program_counter)

# Loop until program counter reaches class size
while program_counter < class_size:
    # Increment program counter by 1
    program_counter += 1
    
    # Print current program counter value
    print("Program Counter:", program_counter)

# Print final message when program counter reaches class size
print("Program Counter stopped at", class_size)
