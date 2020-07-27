def mincostTickets (days, costs):
    dp = [0] * 366
    for i in range (1,max (days)+1):
        if i in days:
            dp[i] = min (dp[i - 1] + costs[0], dp[i - 7] + costs[1], dp[i - 30] + costs[2])
        else:
            dp[i] = dp[i-1]
    return dp[:max (days) + 1][-1]



def mincostTickets2( days, costs):
    dp = [0]*366
    for i in range(1,max(days)+1):
        dp[i] = min(dp[i-1] + costs[0] , dp[i-7] + costs[1], dp[i-30] + costs[2])
    return dp[:max(days)+1][-1]

days = [1,4,6,7,8,20]
costs= [2,7,15]
print (mincostTickets2 (days, costs))

