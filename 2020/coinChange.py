class Classy:
    def __init__(self):
        pass

    def coinExchange(self,coins,amount):
        '''

        :param coinValue:
        :return:
        coins = [1, 2, 5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1

        min(coinNumber[index], )

        0  1  2   3    4    5    6    7     8     9    10      11
        0  1
        '''

        dp = [float('inf')] * (amount+1)

        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
        




coins = [1, 2, 5]
amount = 11
obj = Classy()
print (obj.coinExchange (coins, amount))