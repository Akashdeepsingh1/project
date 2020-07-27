def floodFill ( image, sr: int, sc: int, newColor: int):
    ls = [(sr, sc)]
    visited = []
    while ls:
        r, c = ls.pop()
        image[r][c] = newColor
        visited.append ((r, c))
        for tr, tc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            if 0 <= r + tr < len (image) and 0 <= c + tc < len (image[0]) and image[r + tr][tc + c] != 0 and (r + tr, tc + c) not in visited:
                ls.append ((r + tr, tc + c))
    return image



image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print (floodFill (image, sr, sc, newColor))