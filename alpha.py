# Sentence Calculator
# Calculate the total score (sum of the individual character scores) of a sentence given the following score rules for each allowed group of characters:

# Lower case [a-z]: 'a'=1, 'b'=2, 'c'=3, ..., 'z'=26
# Upper case [A-Z]: 'A'=2, 'B'=4, 'C'=6, ..., 'Z'=52
# Digits [0-9] their numeric value: '0'=0, '1'=1, '2'=2, ..., '9'=9
# Other characters: 0 value
# Note: input will always be a string


import string
def letters_to_numbers(s):
    lower_case = string.ascii_lowercase
    upper_case= string.ascii_uppercase
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    counter = 0
    for char in s:
        if char in lower_case:
            counter += lower_case.index(char) + 1
        elif char in upper_case:
            counter += 2*(upper_case.index(char) + 1)
        elif char in digits:
            counter += int(char)
        else:
            counter += 0
    return counter
