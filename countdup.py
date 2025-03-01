def duplicate_count(text):
    counter = 0
    temp = set()  # Use a set to track characters we've already seen
    duplicates = set()  # Use a set to track duplicates
    
    # Iterate through each character in the lowercased text
    for char in text.lower():
        if char in temp:  # If we've seen this character before, it's a duplicate
            duplicates.add(char)
        else:
            temp.add(char)  # If it's the first time, add it to the 'temp' set
    
    # The length of the duplicates set gives the number of distinct duplicate characters
    return len(duplicates)

# Example usage:
print(duplicate_count("Indivisibilities"))  # Output: 2
