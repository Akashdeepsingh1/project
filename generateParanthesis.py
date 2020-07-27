'''

class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

obj = Solution()
obj.generateParenthesis(3)



Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''







class Solution:
    def __init__(self):
        pass
    def generateParathesis(self,n):
        self.ans = []
        def backTracking(s,left,right):
            if len(s) == 2*n:
                self.ans.append(s[:])
                return
            else:
                if left<n:
                    backTracking(s+'(',left+1,right)
                if right<left:
                    backTracking(s+')',left,right+1)

        backTracking('',0,0)
        return self.ans

    def permutation(self,n):
        self.ans2 = []
        n = list(n)
        def backtracking(s, index ):
            if index == len(n):
                self.ans2.append(''.join(n[:]))
            for i in range(index, len(n)):
                n[i], n[index] = n[index], n[i]
                backtracking(s,index+1)
                n[i], n[index] = n[index], n[i]
        backtracking(n,0)
        return self.ans2




obj = Solution()
print (obj.generateParathesis (3))

print(obj.permutation('abc'))