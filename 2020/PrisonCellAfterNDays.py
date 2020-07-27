def solution(cells, days):
    temp_list = []
    count = 0
    while days>0:
        days-=1
        count+=1
        l_cell = len(cells)
        temp_cell = [0]*l_cell
        for i in range(1, l_cell-1):
            if (cells[i-1] == 0 and cells[i+1] == 0) or  (cells[i-1] == 1 and cells[i+1] == 1):
                temp_cell[i] = 1
        cells = temp_cell
        if cells in temp_list:
            print('{}   {}    {}'.format(cells,'True', count))

        else:
            print ('{}   {} '.format (cells, 'False'))
            temp_list.append (cells[:])

    return cells


def solution2(cells, days):
    temp_list = []
    count = 0
    while count<15:
        days-=1
        count+=1
        l_cell = len(cells)
        temp_cell = [0]*l_cell
        for i in range(1, l_cell-1):
            if (cells[i-1] == 0 and cells[i+1] == 0) or  (cells[i-1] == 1 and cells[i+1] == 1):
                temp_cell[i] = 1
        cells = temp_cell
        print(temp_cell)
        temp_list.append (cells[:])

    if [0,0,1,1,1,1,1,0] in temp_list:
        print('Present')
    else:
        print('Not Present')
    print((days%14)-1)
    return temp_list[(days%14)-1]


    #return cells


def prisonAfterNDays(cells, N):
    def nextday(cells):
        return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1])
                for i in range(8)]

    seen = {}
    while N > 0:
        c = tuple(cells)
        print(c)
        if c in seen:
            print('{}   {}'.format(c,N))
            N %= seen[c] - N
        seen[c] = N
        print ('{}   {}'.format (c, N))

        if N >= 1:
            N -= 1
            cells = nextday(cells)
    for k,v in seen.items():
        print(" {}    {} ".format(k,v))
    return cells


cells = [0,1,0,1,1,0,0,1]
N = 100
#print (solution(cells, N))
print (prisonAfterNDays (cells, N))