def areaofIsland(nums,i,j,count):
    if i<0 or j<0 or len(nums)-1<i or len(nums[0])-1<j or nums[i][j] == 0:
        return count



        nums[i][j] = 0
        areaofIsland(nums,i-1,j-1,count)
        areaofIsland (nums,i - 1, j, count)
        areaofIsland(nums,i-1,j+1,count)

        areaofIsland (nums, i, j - 1, count)
        areaofIsland(nums,i,j+1,count)

        areaofIsland(nums,i+1,j-1,count+1)
        areaofIsland(nums,i+1,j,count+1)
        areaofIsland(nums,i+1,j-1,count+1)

    return count


def areaIsland(nums):
    area = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums[0])):
            if nums[i][j] == 1:
                area.append(areaofIsland(nums,i,j,1))


    return area

nums = [[1,1,0,0,1], [0,1,0,1,1], [1, 0, 0, 1, 1], [1, 0, 0, 0, 0]]
print (areaIsland (nums))





'''
def islandCount (mat):
    arr = []
    for i in range (len (mat)):
        for j in range (len (mat[i])):
            if mat[i][j] == 1:
                arr.append (dfs (mat, i, j, arr))

    nArr = []
    for i in range (len (arr)):
        if (arr[i] != 0): nArr.append (arr[i])

    return nArr


def dfs (mat, i, j, arr):
    if (i < 0 or i >= len (mat) or j < 0 or j >= len (mat[i]) or mat[i][j] == 0):
        return arr[len (arr) - 1]

    if (mat[i][j] == 1):
        mat[i][j] = 0

        if arr == []:
            arr.append (1)
        else:
            arr[len (arr) - 1] = arr[len (arr) - 1] + 1

        # print(arr)
        dfs (mat, i, j + 1, arr)
        dfs (mat, i, j - 1, arr)
        dfs (mat, i + 1, j, arr)
        dfs (mat, i - 1, j, arr)
        dfs (mat, i + 1, j - 1, arr)
        dfs (mat, i + 1, j + 1, arr)
        dfs (mat, i - 1, j - 1, arr)
        dfs (mat, i - 1, j + 1, arr)

    arr.append (0)
    return arr[len (arr) - 1]


print (islandCount ([[1, 1, 0, 0, 1], [0, 1, 0, 1, 1], [1, 0, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1]]))

'''