# The galactic games have begun!
# It's the galactic games! Beings of all worlds come together to compete in several interesting sports, like nroogring, fredling and buzzing (the beefolks love the last one). However, there's also the traditional marathon run.

# Unfortunately, there have been cheaters in the last years, and the committee decided to place sensors on the track. Committees being committees, they've come up with the following rule:

# A sensor should be placed every 3 and 5 meters from the start, e.g. at 3m, 5m, 6m, 9m, 10m, 12m, 15m, 18m….

# Since you're responsible for the track, you need to buy those sensors. Even worse, you don't know how long the track will be! And since there might be more than a single track, and you can't be bothered to do all of this by hand, you decide to write a program instead.

# Task
# Return the sum of the multiples of 3 and 5 below a number. Being the galactic games, the tracks can get rather large, so your solution should work for really large numbers (greater than 1,000,000).

def sum_divisible_by(n, limit):
    p = (limit - 1) // n # p is the count of multiples of n that are less than limit.
    return n * p * (p + 1) // 2 # No loops

def solution(number):
    return sum_divisible_by(3, number) + sum_divisible_by(5, number) - sum_divisible_by(15, number)



print(solution(10))