def searchMatrix (matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    c = len (matrix[0])
    r = len (matrix)

    i = 0
    while (i < c and i < r):
        if matrix[i][i] == target:
            return True
        elif matrix[i][i] < target:
            i += 1
        else:
            for j in range (c - (c - i)):
                if matrix[i][j] == target:
                    return True

            for j in range (r - (r - i)):
                if matrix[j][i] == target:
                    return True
            i+=1
    while i < r:
        if matrix[i][r-i] == target:
            return True
        elif matrix[1][r-i] < target:
            i += 1
        else:
            for i in range (c):
                if matrix[r - 1][i] == target:
                    return True
            i+=1
    while i < c:
        if matrix[i][c - 1] == target:
            return True
        elif matrix[i][c - 1] < target:
            i += 1
        else:
            for i in range (r):
                if matrix[i][c - 1] == target:
                    return True
            i+=1
    return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30],[31,32,33,34,35]]
target = 33
print (searchMatrix (matrix, target))