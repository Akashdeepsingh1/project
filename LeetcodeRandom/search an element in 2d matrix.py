def searchin2D(matrix, target):
    r = len(matrix) - 1
    col = 0
    c_lim = len(matrix[0])

    while r>=0 and col < c_lim:
        x = matrix[r][col]
        print(x)
        if x== target:
            return True
        elif x>= target:
            r-=1
        else:
            col+=1

    return False







mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[18,21,23,26,30]]
mat1 = [[1],[3],[5]]
mat2 = [[1],[3]]
target = 5

print(searchin2D(mat,target))