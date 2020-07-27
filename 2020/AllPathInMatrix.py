'''allPaths = []


def findPaths (maze, m, n):
    path = [0 for d in range (m + n - 1)]
    findPathsUtil (maze, m, n, 0, 0, path, 0)


def findPathsUtil (maze, m, n, i, j, path, indx):
    global allPaths
    # if we reach the bottom of maze, we can only move right
    if i == m - 1:
        for k in range (j, n):
            # path.append(maze[i][k])
            path[indx + k - j] = maze[i][k]
            # if we hit this block, it means one path is completed.
        # Add it to paths list and print
        print (path)
        allPaths.append (path)
        return
    # if we reach to the right most corner, we can only move down
    if j == n - 1:
        for k in range (i, m):
            path[indx + k - i] = maze[k][j]
            # path.append(maze[j][k])
        # if we hit this block, it means one path is completed.
        # Add it to paths list and print
        print (path)
        allPaths.append (path)
        return

    # add current element to the path list
    # path.append(maze[i][j])
    path[indx] = maze[i][j]

    # move down in y direction and call findPathsUtil recursively
    findPathsUtil (maze, m, n, i + 1, j, path, indx + 1)

    # move down in y direction and call findPathsUtil recursively
    findPathsUtil (maze, m, n, i, j + 1, path, indx + 1)


if __name__ == '__main__':
    maze = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    findPaths (maze, 3, 3)

'''


class Solution:
    def __init__(self):
        pass

    def path(self, matrix):
        temp_matrix = [[ "" for i in range(len(matrix))] for j in range(len(matrix[0]))]
        temp_matrix[0][0] = list(matrix[0][0])
        for i in range(1,len(matrix)):
            temp_matrix[0][i] = list(temp_matrix[0][i-1][0] + str(matrix[0][i]))
        for j in range(1,len(matrix[0])):
            temp_matrix[j][0] = list(temp_matrix[j-1][0][0] + str(matrix[j][0]))

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                    temp = []
                    #a = temp_matrix[i-1][j]
                    temp.extend([temp_matrix[i-1][j]])
                    temp.extend([temp_matrix[i][j-1]])
                    for k in range(len(temp)):
                        temp[k] +=str(matrix[i][j])
                    temp_matrix[i][j] = temp


        return temp_matrix



    def allPath(self,matrix):
        temp_matrix = [[[] for i in range(len(matrix))] for j in range(len(matrix))]
        temp_matrix[0][0].append(matrix[0][0])
        for i in range(1,len(matrix)):
            temp_matrix[i][0] = [temp_matrix[i-1][0][0]+matrix[i][0]]

        for i in range (1, len (matrix[0])):
            temp_matrix[0][i] = [temp_matrix[0][i-1][0] + matrix[0][i]]

        for i in range(1,len(matrix)):

            for j in range(1,len(matrix)):
                temp = []
                temp.extend(temp_matrix[i-1][j])
                temp.extend(temp_matrix[i][j-1])
                temp_matrix[i][j] = [each + matrix[i][j] for each in temp]

        return temp_matrix

matrix = [['a','b','c'],['d','e','f'],['i','j','k']]
obj = Solution()
#print (obj.path (matrix))
print (obj.allPath (matrix))





