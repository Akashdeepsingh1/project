def differentBytes(a, b):
    a_dis = bin(a)[2:]
    b_dis = bin(b)[2:]
    print(a_dis)
    print(b_dis)

    count = 0
    for i in range(1, min(len(a_dis), len(b_dis))+1):
        if a_dis[-i] != b_dis[-i]:
            count += 1

    if len(a_dis) < len(b_dis):
        a_dis, b_dis = b_dis, a_dis

    for i in range(len(a_dis)-len(b_dis)):
        if a_dis[i] == '1':
            count += 1

    return count


print(differentBytes(1, 4))
