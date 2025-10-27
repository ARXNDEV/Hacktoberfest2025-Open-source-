# Coin Change Problem II
def count(coins, n, total):
    dp = [0] * (total + 1)
    dp[0] = 1  # one way to make sum 0 (no coins)

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] += dp[amount - coin]

    return dp[total]
