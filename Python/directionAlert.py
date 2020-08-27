def isRobotBounded(instructions: str) -> bool:
    if not instructions:
        return None

    count = 0
    visited = set()
    current = [[(0, 0), 0]]
    total_count = 0
    prev = None
    e, w, n, s = (0, 1), (0, -1), (1, 0), (-1, 0)
    # 0,1,2,3 = 'e','n','w','s'

    l = [0, 1, 2, 3]

    while total_count < 100:
        currentPoint, direction = current.pop()
        if currentPoint in visited:
            print('True')
        if direction != prev:
            print('True')
        if currentPoint in visited and direction != prev:
            return True

        temp = instructions[count]
        visited.add(currentPoint)
        prev = currentPoint
        if temp == 'G':
            if direction == 0:
                currentPoint = (currentPoint[0], currentPoint[1] + 1)
            elif direction == 1:
                currentPoint = (currentPoint[0], currentPoint[1] - 1)
            elif direction == 2:
                currentPoint = (currentPoint[0] + 1, currentPoint[1])
            else:
                currentPoint = (currentPoint[0] - 1, currentPoint[1])

        elif temp == 'L':
            direction = l[(direction+1) % 4]
        else:
            direction = l[(direction+3) % 4]
        count += 1
        current.append([currentPoint, direction])
        if count == len(instructions):
            total_count += count
            count = 0
    return False


direc = 'GGLLGG'
print(isRobotBounded(direc))
