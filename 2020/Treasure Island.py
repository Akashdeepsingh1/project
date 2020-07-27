'''

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.

'''

from queue import Queue

def solution(island):
    q = Queue()
    island[0][0] = 0
    q.put((0,0,0,[[0,0]]))

    while q.qsize()>0:
        x,y,distance, path = q.get()
        for (i,j) in[(-1,0),(1,0),(0,1),(0,-1)]:
            if 0>x+i or x+i>=len(island) or 0>y+j or y+j>=len(island[0]) or island[x+i][y+j] == 'D':
                continue
            elif island[x+i][y+j] == 'X':
                return (distance+1,path)
            else:
                if island[x+i][y+j] == 'O':
                    island[x + i][y + j] = distance + 1
                    q.put ((x + i, y + j, distance + 1, path + [[x+i,y+j]]))
                elif island[x+i][y+j]>distance+1:
                    island[x+i][y+j] = distance+1
                    q.put ((x + i, y + j, distance + 1, path + [[x + i,y + j]]))
                else:
                    q.put((x + i, y + j, distance + 1, path))


    return 0


d = [['O', 'O', 'O', 'O'],['D', 'O', 'D', 'O'],['O', 'O', 'O', 'O'],['O', 'D', 'D', 'X']]

print (solution (d))


