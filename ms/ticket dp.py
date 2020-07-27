class Solution:
    def mincostTickets(self, days, costs):
        if not days:
            return 0
        if len (days) == 1:
            return min (costs)
        n = max (days)
        dp = [0] * (366)

        for i in range (1, n + 1):
            if i in days:
                dp[i] = min (dp[i - 1] + costs[0], dp[i - 7] + costs[1], dp[i - 30] + costs[2])

            else:
                dp[i] = dp[i - 1]
        return dp[:n + 1][-1]



obj = Solution()
days = [1,4,6,7,8,20]
costs = [2,7,15]


print (obj.mincostTickets (days, costs))
