def cubeRoot(x, k):
    """
    :type x: int
        :type k: float
    :rtype: float
    """

    temp_value = float(x)
    res = 0

    while abs(temp_value * temp_value * temp_value - x) > k:
        temp_value = (temp_value + x / temp_value / temp_value) / 2

    res = temp_value

    return res


print(cubeRoot(100, 3))
