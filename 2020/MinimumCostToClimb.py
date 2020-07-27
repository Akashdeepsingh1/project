def minCost(cost):
    '''

    :param cost:
    :return:

    Example 1:
    Input: cost = [10, 15, 20]
    Output: 15
    Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
    Example 2:
    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6
    Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

    '''
    if not cost:
        return 0

    from collections import defaultdict
    cost.append(0)
    d = defaultdict(int)
    d[0] = cost[0]
    d[1] = cost[1]
    d[2] = min(cost[0],cost[1]) + cost[2]
    for i in range(3,len(cost)):
        d[i] = cost[i]+ min(d[i-1],d[i-2])

    return d[len(cost)-1]

cost1 = [10,15,20]
print (minCost (cost1))

cost2 = [1,100,1,1,1,100,1,1,100,1]
print(minCost(cost2))

cost3 = [0,0,0,1]
print(minCost(cost3))