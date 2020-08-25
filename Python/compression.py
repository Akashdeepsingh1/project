'''
s = abaasass
r = aba2sas2

'''


def compression(inputString):
    if not inputString:
        return None

    result = ""
    count = 0
    current = ""

    for each in inputString:
        if not current:
            current = each
            count = 1
        elif current != each:
            result += str(current)
            if count > 1:
                result += str(count)
            current = each
            count = 1
        else:
            count += 1
    result += str(current)
    if count > 1:
        result += str(count)

    return result


s = "abaasass"
print(compression(s))
