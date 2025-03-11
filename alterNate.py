# Create a function that accepts a string as an argument and validates whether the vowels (a, e, i, o, u) and consonants are in alternate order.

# Examples
# "amazon" --> true
# "apple" --> false
# "banana" --> true


def is_alt(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}  
    for i in range(len(s) - 1):
        if (s[i] in vowels) == (s[i + 1] in vowels):
            return False
    return True