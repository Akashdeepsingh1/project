def repeatedStringMatch (A: str, B: str) -> int:
    # lenA = len(A)
    # lenB = len(B)
    #
    #
    #
    # if lenA > lenB:
    #     if B in A:
    #         return 1
    # else:
    #     a = A
    #     count = 1
    #     FLAG = True
    #     while lenA < 1000:
    #         if FLAG:
    #             a = a + A
    #             FLAG = False
    #         else:
    #             a = A + a
    #             FLAG = True
    #         count += 1
    #         lenA = len(a)
    #         if B in a:
    #             return count
    #
    #     return -1
    for i in range (int(len (B) / len (A)), int(len (B) / len (A)) + 3):
        if B in i * A:
            return i
    return -1



print(repeatedStringMatch('a*1000000000000000000','aaaaaaaaaaaaaaaaaaaaaaaa'))
#repeatedStringMatch('abaabaa','abaababaab')