class Solution:
    def cutOffTree(self, forest) -> int:
        l = set()
        #l.add((0,0))
        visited = set()
        Flag = True
        final_count = 0
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if Flag:
                    l.add((0,0,0))
                    Flag = False
                    while l:
                        r,c,count = l.pop()
                        forest[r][c] = 0
                        visited.add((r,c))
                        for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
                            if 0<=(i+r)<len(forest) and 0<= (j+c)<len(forest[0]) and (i+r,j+c) not in visited and forest[i+r][j+c]!=0:
                                l.add((i+r,j+c,count+1))
                                if final_count < count+1:
                                    final_count = count+1
                else:
                    if forest[i][j]!=0:
                        return -1
        return final_count



obj = Solution()
t = [[1,2,3],[0,0,0],[7,6,5]]
print (obj.cutOffTree (t))