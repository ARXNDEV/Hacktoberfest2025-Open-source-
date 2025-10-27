
# Minimum Number of Coins - Coin Change

def minCoins(value, coins):
    # Initialize dp array with a large number (value+1 is a safe upper bound)
    dp = [value + 1] * (value + 1)
    dp[0] = 0  # 0 coins needed to make amount 0

    for amount in range(1, value + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[value] if dp[value] != value + 1 else -1
