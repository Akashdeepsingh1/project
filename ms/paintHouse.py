def minCost (costs) -> int:
    if not len (costs):
        return 0
    lastR, lastG, lastB = costs[0][:]
    for i in range (1, len (costs)):
        curR = min (lastG, lastB) + costs[i][0]
        curG = min (lastR, lastB) + costs[i][1]
        curB = min (lastR, lastG) + costs[i][2]
        lastR, lastG, lastB = curR, curG, curB

    return min (lastR, lastG, lastB)

t = [[17,2,17],[16,16,5],[14,3,19]]
print (minCost (t))