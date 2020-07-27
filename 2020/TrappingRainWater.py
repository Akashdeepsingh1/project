def trappingRainWater(steps):
    '''

    :param steps: Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    :return: 6
    '''

    l = 0
    r = len(steps) - 1
    left_max , right_max = 0,0
    result = 0
    while l<r:
        if steps[l]<steps[r]:
            if left_max < steps[l]:
                left_max = steps[l]
            else:
                result += (left_max - steps[l])
            l+=1
        else:
            if right_max < steps[r]:
                right_max = steps[r]
            else:
                result += (right_max - steps[r])
            r -= 1
    return result


steps = [0,1,0,2,1,0,1,3,2,1,2,1]
print (trappingRainWater (steps))