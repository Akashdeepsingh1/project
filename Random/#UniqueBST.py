def uniqueBST(node):
    if not node or node == 0:
        return 0
    if node == 1:
        return 1
    else:
        dp = [0]*(node+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, node+1):
            for j in range(1, i+1):
                dp[i] += (dp[j-1] * dp[i-j])
        return dp[-1]


print(uniqueBST(1))
print(uniqueBST(2))
print(uniqueBST(3))
print(uniqueBST(4))
print(uniqueBST(5))
print(uniqueBST(6))
