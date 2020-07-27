def uniquePaths (m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    dp = [[1 for _ in range (m)] for _ in range (n)]
    print (dp)
    for i in range (1, n):
        for j in range (1, m):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


print (uniquePaths (3, 2))