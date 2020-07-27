class Classy:
    def __init__(self):
        pass


    def island(self,matrix):
        if not matrix:
            return 0
        count = 0


        from collections import deque
        self.visited= []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) in self.visited:
                    continue
                if matrix[i][j]=='1':
                    d = deque()
                    d.append((i,j))
                    count+=1
                    while d :
                        item = d.pop()
                        matrix[item[0]][item[1]] = '0'
                        for each in [-1,0],[0,-1],[1,0],[0,1]:
                            x, y = each[0]+item[0], each[1] + item[1]
                            if 0<=x<len(matrix) and 0<=y<len(matrix[0])and (x,y) not in self.visited:
                                if matrix[x][y] == '1':
                                    d.append((x,y))
                                self.visited.append((x,y))
                else:
                    self.visited.append((i,j))
        return count

obj = Classy()
mat = [["1","0","0","1","0"],["0","1","0","1","0"],["1","0","0","0","0"],["0","0","0","0","1"]]
print (obj.island (mat))
