def minimumcostpath(m):

    row = len(m)
    col = len(m[0])

    sum_m= [[0 for i in range(0,col)] for j in range(0,row)]
    sum_m[0][0] = m[0][0]

    for i in range(1,col):
        temp = m[0][i] + sum_m[0][i-1]
        sum_m[0][i]  = temp

    for i in range(1,row):
        temp = m[i][0] + sum_m[i-1][0]
        sum_m[i][0] = temp

    for i in range(1,col):
        for j in range(1,row):
            print(sum_m[j][i-1])
            
            sum_m[i][j] = m[i][j] + min(sum_m[j][i-1],sum_m[i-1][j])


    print(sum_m[row-1][col-1])


minimumcostpath([[1,2,5],[3,2,1]])
