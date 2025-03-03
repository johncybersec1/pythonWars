# It's time to create an autocomplete function! Yay!

# The autocomplete function will take in an input string and a dictionary array and return the values from the dictionary that start with the input string. If there are more than 5 matches, restrict your output to the first 5 results. If there are no matches, return an empty array.

# Example:

# autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']
# For this kata, the dictionary will always be a valid array of strings. Please return all results in the order given in the dictionary, even if they're not always alphabetical. The search should NOT be case sensitive, but the case of the word should be preserved when it's returned.

# For example, "Apple" and "airport" would both return for an input of 'a'. However, they should return as "Apple" and "airport" in their original cases.
def autocomplete(input_, dictionary):
    input_clean = ''.join([char.lower() for char in input_ if char.isalpha()]) 
    
    matches = [word for word in dictionary if word.lower().startswith(input_clean)]
    
    return matches[:5]