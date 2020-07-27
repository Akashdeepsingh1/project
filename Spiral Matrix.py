'''

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


'''


class Solution:
    def __init__(self):
        pass
    def spiralMatrix(self,n):
        count = 0
        max_val =n**2
        import copy
        matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        #matrix=copy.deepcopy(matrix)
        i, j = 0,0
        while count <= max_val:
            for horizontal_runner in range(i,n-i):
                matrix[i][horizontal_runner] = count
                count+=1

            for vertical_runner in range(i+1,n-i):
                matrix[n-i-1][vertical_runner] = count
                count +=1

            for reverse_horizontal_runner in range(n-i-1,i,-1):
                matrix[n-i-1][reverse_horizontal_runner-1] = count
                count+=1

            for reverse_vertical_runner in range(n-i-1,i,-1):
                matrix[reverse_vertical_runner][i] = count
                count+=1
            i+=1
        return matrix

obj= Solution()
print (obj.spiralMatrix (4))