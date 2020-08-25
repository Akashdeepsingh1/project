def findCircle(m):
    if not m or not m[0]:
        return None

    visited = [0] * len(m)
    queue = []
    circle = 0
    for i in range(len(m)):
        if visited[i] == 0:
            queue.append(i)

            while queue:
                item = queue[0]
                visited[item] = 1
                del queue[0]
                for j in range(len(m)):
                    if m[item][j] == 1 and not visited[j]:
                        queue.append(j)
            circle += 1
    return circle


m1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
m2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
m3 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]

print(findCircle(m1))
print(findCircle(m2))
print(findCircle(m3))
