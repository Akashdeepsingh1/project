def uniquePathsWithObstacles ( obstacleGrid) -> int:
    m = len (obstacleGrid[0])
    n = len (obstacleGrid)

    dp = [[1 for _ in range (m)] for _ in range (n)]
    for i in range (m):
        if obstacleGrid[0][i] == 1:
            dp[0][i] = 0

    for j in range (n):
        temp = obstacleGrid[j][0]
        if temp == 1:
            dp[j][0] = 0

    for i in range (1, n):
        for j in range (1, m):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


og = [[1,0]]
print (uniquePathsWithObstacles (og))
