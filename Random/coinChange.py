def coinChange(coins, amount) -> int:
    if not coins or not amount:
        return None
    dp = [float('inf')] * (amount+1)
    for i in range(1, amount+1):
        if i in coins:
            dp[i] = 1
        else:
            #dp[i] = float('inf')
            for coin in coins:
                dp[i] = min(dp[i-coin]+1, dp[i])


coins = [1, 2, 5]
amount = 11

coins1 = [2]
amount1 = 3
coinChange(coins1, amount1)
