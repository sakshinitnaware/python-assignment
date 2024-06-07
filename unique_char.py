def unique_characters(string):
    # Initialize an empty string to store unique characters
    unique_chars = ""
    
    # Iterate through each character in the input string
    for char in string:
        # Check if the character is not already in the unique_chars string
        if char not in unique_chars:
            # If the character is not in unique_chars, add it to the unique_chars string
            unique_chars += char
    
    # Return the string containing unique characters
    return unique_chars

# Test the function
input_string = input("Enter a string: ")  # Take input from the user
result_string = unique_characters(input_string)  # Call the function with the input string
print("String with unique characters:", result_string)  # Print the result
