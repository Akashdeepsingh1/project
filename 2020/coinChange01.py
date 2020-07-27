class Classy:
    def __init__(self):
        pass


    def coinChange(self,coins,amount):

        '''
        :param coins:
        :param amount:
        :return:

        Example 1:

        Input: coins = [1, 2, 5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1
        Example 2:

        Input: coins = [2], amount = 3
        Output: -1
        '''
        if not coins or amount == 0:
            return -1

        d = [float('inf')]*(amount+1)

        d[0] = 0

        for coin in coins:
            for i in range(coin,amount+1):
                d[i] = min(d[i], d[i-coin] + 1)
        if d[amount] == float('inf'):
            return -1
        return d[amount]


coins = [1, 2, 5]
amount = 11

obj = Classy()
print (obj.coinChange (coins, amount))