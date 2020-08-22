class Solution:
    def __init__(self):
        self.perimeter = 0
        self.island = []
        self.common = 0
        self.visited = set()
        self.queue = []

    def perimeterIsland(self, i, j):
        self.queue.append((i, j))
        while self.queue:
            i, j = self.queue.pop()

            if i < 0 or j < 0 or i > len(self.island) or j > len(self.island[0]) or (i, j) in self.visited or self.island[i][j] == 0 or (i, j) in self.queue:
                continue
            self.perimeter += 1
            self.visited.add((i, j))
            if i > 0 and self.island[i-1][j] == 1:
                self.common += 1
                self.queue.append((i-1, j))
            if j > 0 and self.island[i][j-1] == 1:
                self.common += 1
                self.queue.append((i, j-1))
            if i < len(self.island)-1 and self.island[i+1][j] == 1:
                self.common += 1
                self.queue.append((i+1, j))
            if j < len(self.island[0])-1 and self.island[i][j+1] == 1:
                self.common += 1
                self.queue.append((i, j+1))

    def startPoint(self, matrix):
        self.island = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    self.perimeterIsland(i, j)
                    print(self.perimeter)
                    print(self.common)
                    return self.perimeter * 4 - self.common


obj = Solution()
matrix = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(obj.startPoint(matrix))
