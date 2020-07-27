class Classy:
    def __init__(self):
        pass

    def zombieLand(self, matrix):
        if not matrix:
            return 0

        self.visited = set()
        from collections import deque
        d = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    d.append((i,j))


        count = 0
        while d:
            temp = []
            count += 1
            while d:
                item = d.pop()
                self.visited.add(item)
                for i,j in (-1,0),(0,-1),(1,0),(0,1):
                    if 0<=item[0] + i <len(matrix) and 0<= item[1]+ j < len(matrix[0]) and (item[0] + i,item[1]+ j) not in self.visited:
                        matrix[item[0]+i][item[1]+j] = 1
                        temp.append((item[0]+i,item[1]+j))
            d.extend(temp)
        return count-1, self.visited, len(self.visited)

obj = Classy()
matrix = [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]
print (obj.zombieLand (matrix))