'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

'''


def wordBreak (s, wordDict):
    s_l = list (s)
    i = 0
    #Flag = True
    while i < len(s_l):

        for j in range (i, len (s)):
            s = ''.join (s_l[i:j + 1])
            if s in wordDict:
                for k in range (i, j + 1):
                    s_l[k] = "0"
                    i = j+1
        i+=1
    for each in s_l:
        if each != "0":
            return False
    return True

s = "leetcode"
wordDict = ["leet", "code"]
print (wordBreak (s, wordDict))

S1 = "applepenapple"
wordDict1 = ["apple", "pen"]

print(wordBreak(S1,wordDict1))


s2 = "catsandog"
wordDict2 = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s2,wordDict2))
