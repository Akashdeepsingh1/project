class Solution:

    def wallsAndGates (self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        r = len (rooms)
        c = len (rooms[0])
        if r == 0 or c == 0:
            return 0

        def bfs (room, i, j, counter):
            if room[i][j] != 2147483647:
                return room[i][j]
            l = [[i, j, 0]]
            temp_counter = 0

            while len (l) > 0 and temp_counter<counter:
                temp = []
                while len (l) > 0:
                    temp_counter+=1
                    temp_i, temp_j, count = l.pop()
                    if room[temp_i][temp_j] == 0:
                        return count
                    else:
                        # add all four corners in temp
                        if temp_i > 0 and room[temp_i-1][temp_j]!= -1:
                            temp.append ([temp_i - 1, temp_j, count+1])
                        if temp_j > 0 and room[temp_i][temp_j-1]!= -1:
                            temp.append ([temp_i, temp_j - 1, count+1])
                        if temp_i < len (room) - 1 and room[temp_i+1][temp_j]!=-1:
                            temp.append ([temp_i + 1, temp_j, count+1])
                        if temp_j < len (rooms[0]) - 1 and room[temp_i][temp_j+1] != -1:
                            temp.append ([temp_i, temp_j + 1, count+1])

                l = temp
            return 2147483647

        for i in range (r):
            for j in range (c):
                if rooms[i][j] == 2147483647:
                    temp = bfs (rooms, i, j, r*c)
                    rooms[i][j] = min (temp, rooms[i][j])

        return rooms


'''
    def wallsAndGates (self, rooms) -> None:
        # edge case
        if not rooms:
            return []
        # Initialize the queue with all 0s
        from collections import deque
        R, C = len (rooms), len (rooms[0])
        q = deque ()
        for r in range (R):
            for c in range (C):
                if rooms[r][c] == 0:
                    q.append ((r, c))

        while q:
            r, c = q.popleft ()
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= r + x < R and 0 <= c + y < C and rooms[r + x][c + y] > rooms[r][c]:
                    rooms[r + x][c + y] = rooms[r][c] + 1
                    q.append ((r + x, c + y))

'''
obj = Solution()
temp = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
temp1 = [[2147483647,2147483647],[2147483647,2147483647]]
obj.wallsAndGates(temp1)


