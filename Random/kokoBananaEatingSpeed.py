'''
Input: piles = [3,6,7,11], H = 8
Output: 4
Input: piles = [30,11,23,4,20], H = 5
Output: 30
Input: piles = [30,11,23,4,20], H = 6
Output: 23

'''


def kokoBanana(piles, h):
    if not piles or not h:
        return None

    def checkSpeed(middle):
        if not middle:
            return None
        stack = piles[:]
        total_sum = 0
        hours = 1
        while stack:
            item = stack.pop()
            if 2*mid > item:
                total_sum += item
            else:
                total_sum += mid
                stack.append(item-mid)
            hours += 1
            if hours > h:
                return False
        return True

    l = 1
    r = max(piles)

    while l < r:
        mid = l+(r-l)//2
        if checkSpeed(mid):
            r = mid
        else:
            l = mid+1
    return l


piles = [3, 6, 7, 11]
H = 8
Output = 4
print(kokoBanana(piles, H))


piles1 = [30, 11, 23, 4, 20]
H1 = 5
print(kokoBanana(piles1, H1))

piles2 = [30, 11, 23, 4, 20]
H2 = 6
print(kokoBanana(piles2, H2))
