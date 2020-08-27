def checkPalindrome(inputString):
    if not inputString:
        return False

    l = len(inputString)-1

    if l == 0:
        return True

    for i in range((l//2)+1):
        if inputString[i] != inputString[l-i]:
            return False
    return True


def countSubString(s):
    if not s:
        return None
    count = 0
    visitedTrue = set()
    visitedFalse = set()
    l = len(s)
    for i in range(l):
        for j in range(i+1, l+1):
            temp_s = s[i:j]
            if temp_s in visitedTrue:
                count += 1
            elif temp_s in visitedFalse:
                pass
            else:
                if checkPalindrome(temp_s):
                    visitedTrue.add(temp_s)
                    count += 1
                else:
                    visitedFalse.add(temp_s)

    return count


s = 'abc'
print(countSubString(s))
s1 = 'aaa'
print(countSubString(s1))
