def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result

# Test the function
input_string = input("Enter a string: ")
result_string = remove_vowels(input_string)
print("String without vowels:", result_string)
