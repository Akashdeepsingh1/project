from queue import Queue
def wallsAndGates (rooms) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    q = Queue()

    for i in range (len (rooms)):
        for j in range (len (rooms[0])):
            if rooms[i][j] == 0:
                q.put((i,j,1))


    while q.qsize()>0:
        x,y , dis= q.get()
        for (i,j) in ((-1,0),(1,0),(0,-1),(0,1)):
            if x+i < 0 or y+j < 0 or x+i >= len (rooms) or y+j >= len (rooms[0]) or rooms[x+i][y+j] == -1:
                continue
            elif rooms[x+i][y+j] > rooms[x][y]+1:
                rooms[x + i][y + j] = dis
                q.put((x+i,j+y, dis +1))
    return rooms


def wallsAndGates2 (rooms):
    """
    :type rooms: List[List[int]]
    :rtype: None Do not return anything, modify rooms in-place instead.
    """

    def dfs (rooms, i, j, d):
        if not (0 <= i < len (rooms)) or \
                not (0 <= j < len (rooms[0])) or \
                rooms[i][j] < d:
            return

        rooms[i][j] = min (d, rooms[i][j])
        dfs (rooms, i + 1, j, d + 1)
        dfs (rooms, i - 1, j, d + 1)
        dfs (rooms, i, j + 1, d + 1)
        dfs (rooms, i, j - 1, d + 1)

    for i in range (len (rooms)):
        for j in range (len (rooms[0])):
            if rooms[i][j] == 0:
                dfs (rooms, i, j, 0)

    return rooms



rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

print (wallsAndGates (rooms))

print(wallsAndGates2(rooms))