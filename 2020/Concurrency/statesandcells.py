'''class Solution:
    def prisonAfterNDays(self, cells, N):
        def nextday(cells):
            return [int(i > 0 and i < N and cells[i-1] == cells[i+1])
                    for i in range(N+1)]

        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N

            if N >= 1:
                N -= 1
                cells = nextday(cells)

        return cells
'''

'''

def generalized(num,arr):
    temp_min = min(arr)
    temp_max = max(arr)



    if temp_min == temp_max:
        return temp_min
    else:
        for i in range(num):
            if arr[i]>=temp_min:
                arr[i]-= temp_min
        return generalized(num,arr)


print (generalized (5, [2, 3, 4, 5, 6]))
'''




class Solution:
    def prisonAfterNDays(self, cells, N):
        def nextday(cells):
            return [int(i > 0 and i < 7 and cells[i-1] != cells[i+1])
                    for i in range(8)]

        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N

            if N >= 1:
                N -= 1
                cells = nextday(cells)

        return cells


obj = Solution()
cells = [1,0,0,0,0,1,0,0]
days = 1
print (obj.prisonAfterNDays (cells, days))