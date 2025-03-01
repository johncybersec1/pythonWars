def dirReduc(arr):
    result = []  # Use result to track directions

    # Define opposites
    opposites = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST'
    }

    # Iterate through the directions in the array
    for direction in arr:
        if result and result[-1] == opposites[direction]:
            result.pop()  # Cancel the last direction in the result if opposite
        else:
            result.append(direction)  # Add current direction to the result
    
    return result  # Return None if the list is empty