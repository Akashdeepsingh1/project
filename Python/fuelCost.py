def fuelCost(cities, roads, station, capacity, road, fuel, A, B):
    '''
    start at station 1 
    cities = [[1,40],[2,80],[3,100]]
    station = [[1,40],[2,80], [3,0]]
    roads = {1:()}

    '''
    # to do - not completed
    if not cities or not roads or not station or not capacity:
        return None

    stack = [(0, A, fuel[A], distanceTravelled)]
    min_cost = 0
    visited = set()

    while stack:
        cost, item, prevStationFuelCost = stack.pop()
        for each in roads[item]:
            if fuel[each] == 0 and distanceTravelled + each[0][1] < capacity:
                stack.append((cost+each[0][1]*prevStationFuelCost, each[0]
                              [0], prevStationFuelCost, distanceTravelled + each[0][1]))
            elif fuel[each] > prevStationFuelCost:
                stack.append(
                    (cost+capacity*prevStationFuelCost, each[0][0], each[0][1]))
            elif fuel:
                pass
