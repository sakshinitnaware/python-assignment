# Define the maximum number for the pyramid
max_num = 20

# Loop to print the pyramid
for i in range(1, max_num + 1):
    # Print spaces before the numbers
    print(" " * (max_num - i), end="")
    
    # Print numbers in ascending order
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Move to the next line
    print()
