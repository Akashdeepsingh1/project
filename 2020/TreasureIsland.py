class Classy:
    def __init__(self):
        pass

    def treasureIsland(self, matrix, st_pt):
        '''

        :param matrix:
        :param st_pt:
        :return:
        [['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['O', 'O', 'O', 'O'],
        ['X', 'D', 'D', 'O']]

        '''


        from collections import deque

        que = deque()

        que.append(([0,0],0))
        self.visited = []
        final_count = float('inf')
        while que:
            item,count = que.popleft()
            last_item = item
            for i,j in [-1,0],[0,-1],[1,0],[0,1]:
                if [last_item[0]+i, last_item[1]+j] in self.visited:
                    continue
                if 0<=last_item[0]+i<len(matrix) and 0<=last_item[1]+j<len(matrix):
                    if matrix[last_item[0]+i][last_item[1]+j]== 'X':
                        que.append(([last_item[0]+i,last_item[1]+j],count+1))
                        if final_count >count:
                            result =  [last_item[0]+i,last_item[1]+j],count+1
                            final_count = count
                    elif matrix[last_item[0]+i][last_item[1]+j]== 'D':
                        self.visited.append([last_item[0]+i, last_item[1]+j])
                        continue
                    else:
                        que.append (([last_item[0] + i, last_item[1] + j],count+1))
                        #que.append(item)
                self.visited.append ([last_item[0] + i, last_item[1] + j])
        if final_count < float('inf'):
            return result
        return -1


mat = [['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['O', 'O', 'O', 'O'],
        ['X', 'D', 'D', 'D']]
obj = Classy()
print (obj.treasureIsland (mat, (0,0)))
