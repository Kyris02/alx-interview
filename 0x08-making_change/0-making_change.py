#!/usr/bin/python3
"""
    Given a pile of coins of different values,
    the fewest number of coins needed to
    meet a given amount total are determined.
    Cache is utilised to improve runtime.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a cache to store the minimum number of coins for each total
    cache = {}

    def minCoins(target):
        # Check if the result is already cached
        if target in cache:
            return cache[target]

        # Base case: 0 coins needed to make a total of 0
        if target == 0:
            return 0

        # Initialize the minimum count with a large value
        min_count = float('inf')

        # Iterate through all coin values
        for coin in coins:
            # is coin value is less than or equal to the current total?
            if coin <= target:
                # Recursively calculate the minimum number of coins needed
                count = minCoins(target - coin) + 1
                min_count = min(min_count, count)

        # Cache the result
        cache[target] = min_count

        return min_count

    # Call the recursive function
    result = minCoins(total)

    if result == float('inf'):
        return -1

    return result
