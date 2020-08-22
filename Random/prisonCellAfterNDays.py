def prisoncell(prison, days):
    if not prison:
        return 0
    if not days:
        return prison
    new_state = prison[:]
    new_state[0] = 0
    new_state[-1] = 0
    l = len(prison)

    while days > 0:
        for i in range(1, l-1):
            if prison[i-1] == prison[i+1]:
                new_state[i] = 1
            else:
                new_state[i] = 0
        prison = new_state[:]
        days -= 1
    return prison


cells = [0, 1, 0, 1, 1, 0, 0, 1]
N = 7
print(prisoncell(cells, N))
