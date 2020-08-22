def addDigits(num):
    if not num:
        return 0
    while num >= 10:
        temp_sum = 0
        temp = num
        while temp != 0:
            temp_sum += temp % 10
            temp //= 10
        num = temp_sum
    return num


# O(1) solution

def addDigitO1(num):
    if not num:
        return 0
    if num / 9 == 0:
        return 9
    else:
        return num % 9


print(addDigits(123324123))
print(addDigitO1(123324123))
