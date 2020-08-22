
def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0

    diff = [prices[i+1] - prices[i] for i in range(n-1)]
    dp, dp_max = [0]*(n + 1), [0]*(n + 1)
    for i in range(n-1):
        dp[i] = diff[i] + max(dp_max[i-3], dp[i-1])
        dp_max[i] = max(dp_max[i-1], dp[i])

    return dp_max[-3]


prices = [1, 2, 3, 0, 2]
print(maxProfit(prices))
prices1 = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices1))


# this is brute force to understand the DP
# approach is to find the every single combination and get the biggest sum
# approach 1
def maxProfit1(prices):
    max_profit = float('-inf')

    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit


prices = [1, 2, 3, 1, 4]
print(maxProfit1(prices))
prices1 = [7, 1, 5, 3, 6, 4]
print(maxProfit1(prices1))


# approach 2

def maxProfit2(prices):
    diff = [prices[i+1] - prices[i] for i in range(len(prices)-1)]

    max_profit = float('-inf')
    profit = 0
    for i in range(len(diff)):
        if profit + diff[i] > 0:
            profit += diff[i]
            if profit > max_profit:
                max_profit = profit
        else:
            profit = 0
    return max_profit


prices = [1, 2, 3, 1, 4]  # [1,1,-2,3]
print(maxProfit2(prices))
prices1 = [7, 1, 5, 3, 6, 4]  # [-6,4,-2,3,-2]
print(maxProfit2(prices1))

# buy and sell multiple times


def maxProfitMultipleTimes(prices):
    diff = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
    #profit = 0
    max_profit = 0

    for i in range(len(diff)):
        if diff[i] > 0:
            max_profit += diff[i]
    return max_profit


print(maxProfitMultipleTimes(prices))  # 5
print(maxProfitMultipleTimes(prices1))  # 7


# buy and sell stock with cooldown period

def maxProfitCooldown(prices):
    if not prices or len(prices) <= 1:
        return 0

    #diff = [prices[i+1] - prices[i] for i in range(len(prices)-1)]


def maxProfitCoolDown1(prices):
    if not prices or len(prices) < 2:
        return 0
    n = len(prices)
    diff = [prices[i+1] - prices[i] for i in range(n-1)]

    dp = [0] * (n+1)
    dp_max = [0] * (n+1)

    for i in range(n-1):
        dp[i] = diff[i] + max(dp[i-1], dp_max[i-3])
        dp_max[i] = max(dp[i], dp_max[i-1])

    return dp_max[-3]


pricesCooldown = [1, 2, 3, 0, 2]
print(maxProfitCoolDown1(pricesCooldown))
