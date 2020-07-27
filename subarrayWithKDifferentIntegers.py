'''

Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.
https://leetcode.com/problems/subarrays-with-k-different-integers

Example 1:

Input: s = "pqpqs", k = 2
Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
Example 2:

Input: s = "aabab", k = 3
Output: 0
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26

'''


def solution(s,k):
    dic = {}
    from collections import deque
    count_distinct = 0
    que = deque()
    final_list = []
    for i in range(len(s)):
        if k == count_distinct:
            item = list(que)
            final_list.append(''.join(item))
        if i == 0:
            count_distinct = 1
        elif s[i] not in que:
            count_distinct+=1
        que.append(s[i])

    for i in range(len(s)-1,-1,-1):
        item = que.popleft()
        if item not in que:
            count_distinct-=1
        if count_distinct == k:
            item= list(que)
            final_list.append("".join(item))

    return final_list

s = "pqpqs"
k = 2
print (solution (s, k))