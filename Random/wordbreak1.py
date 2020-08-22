def wordBreak(word, wordDict):
    if not word or not wordDict:
        return 0
    dp = [False] * (len(word)+1)
    dp[0] = True

    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            if dp[i] and word[i:j] in wordDict:
                dp[j] = True
    return dp[-1]


print(wordBreak('leetcode', ['leet', 'code']))


print(wordBreak('leetcode', ['lee', 'code']))
