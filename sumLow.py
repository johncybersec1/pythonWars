def sum_two_smallest_numbers(numbers):
    x = min(numbers)
    numbers.remove(x)
    y = min(numbers)
    return x+y