def calculateMinimumHP ( dungeon) -> int:
    for i in range (1,len (dungeon[0])):
        dungeon[0][i] += dungeon[0][i - 1]
    for j in range (1,len (dungeon)):
        dungeon[j][0] += dungeon[j - 1][0]

    for i in range (1, len (dungeon)):
        for j in range (1, len (dungeon[0])):
            if dungeon[i - 1][j] == 0 or dungeon[i][j - 1] == 0:
                continue
            elif dungeon[i - 1][j] < 0 and dungeon[i][j - 1] < 0:
                dungeon[i][j] += max (dungeon[i - 1][j], dungeon[i][j - 1])
            else:
                dungeon[i][j] += min (dungeon[i - 1][j], dungeon[i][j - 1])

    if dungeon[-1][-1]<0:
        return abs(dungeon[-1][-1]) + 1
    else:
        return dungeon[-1][-1]


dun = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
calculateMinimumHP(dun)