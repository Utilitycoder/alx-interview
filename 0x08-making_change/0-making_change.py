#!/usr/bin/python3

def makeChange(coins, total):
    if total < 0:
        return -1  # Total cannot be met with the given coins

    # Initialize a list to store the minimum number of coins for each total from 0 to 'total'
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0

    for coin in coins:
        for i in range(coin, total + 1):
            # Update dp[i] if using 'coin' leads to a smaller number of coins needed
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

# Example usage:
coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print(result)  # Output should be 3 (using two 5-coins and one 1-coin)
