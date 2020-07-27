'''
Input: ropes = [8, 4, 6, 12]
Output: 58
Explanation: The optimal way to connect ropes is as follows
1. Connect the ropes of length 4 and 6 (cost is 10). Ropes after connecting: [8, 10, 12]
2. Connect the ropes of length 8 and 10 (cost is 18). Ropes after connecting: [18, 12]
3. Connect the ropes of length 18 and 12 (cost is 30).
Total cost to connect the ropes is 10 + 18 + 30 = 58
Example 2:

Input: ropes = [20, 4, 8, 2]
Output: 54
Example 3:

Input: ropes = [1, 2, 5, 10, 35, 89]
Output: 224
Example 4:

Input: ropes = [2, 2, 3, 3]
Output: 20


'''


from queue import PriorityQueue

def solution(l):
    q = PriorityQueue()
    for each in l:
        q.put(each)


    total_sum =0
    while q.qsize() >= 2:
        temp = q.get() + q.get()
        total_sum += temp
        q.put(temp)

    return total_sum



l = [8, 4, 6, 12]
ropes = [2, 2, 3, 3]
k = [1, 2, 5, 10, 35, 89]
print (solution (l))
print(solution(ropes))
print(solution(k))
