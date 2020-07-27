'''

Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

Example:

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
int minHours(int rows, int columns, List<List<Integer>> grid) {

}


'''


def solution(input_matrix):
    count_hours = 0
    FLAG = True

    while FLAG:
        list_val = []
        FLAG = False
        for i in range(len(input_matrix)):
            for j in range(len(input_matrix[0])):
                if input_matrix[i][j] == 1:
                    list_val.append((i,j))
                elif input_matrix[i][j] == 0:
                    FLAG = True
        if FLAG:
            count_hours+=1
            for each in list_val:
                i,j = each
                if i-1 >=0 and input_matrix[i-1][j] == 0 :
                    input_matrix[i-1][j] = 1
                if i+1<len(input_matrix) and input_matrix[i+1][j] == 0:
                    input_matrix[i+1][j] = 1
                if j-1>= 0 and input_matrix[i][j-1] == 0:
                    input_matrix[i][j-1] = 1
                if j+1<len(input_matrix[0]) and input_matrix[i][j+1] == 0:
                    input_matrix[i][j+1] = 1
        print(input_matrix)

    return count_hours

input_matrix = [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

print (solution (input_matrix))