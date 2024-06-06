def count_vowels(string):             # defining a function which has input as string.
    vowels = 'aeiouAEIOU'             # defining vowels in upper and lower case.
    vowel_count = 0                   # initializing vowel_count as 0 to increment it later.
    for char in string :              # for loop to itrate over each char in the given string.
        if char in vowels :           # if condition to check that the string has vowel.
            vowel_count += 1          # incrementing the count of vowel is its present in the string.
    return vowel_count                # returing the total count of vowel.
string = str("Guvi Geeks Network Private Limited")      # initializing string input as "Guvi Geeks Network Private Limited".
print("total no. of vowel : ", count_vowels(string))    # printing the total count of vowel which should be 12.
