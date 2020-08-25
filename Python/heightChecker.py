def heightChecker(heights):
    if not heights:
        return None
    count = 0
    temp_array = heights[:]
    temp_array.sort()

    for i in range(len(heights)):
        if heights[i] != temp_array[i]:
            count += 1
    return count


heights = [1, 1, 4, 2, 1, 3]
print(heightChecker(heights))
