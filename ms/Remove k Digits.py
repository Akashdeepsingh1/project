def solution(nums, k):
    if len(nums)==0:
        return 0
    if len(nums) == k:
        return 0

    while k>0:
        dic = {}
        ls = []
        for i in range(len(nums)):
            temp = int(nums[:i] + nums[i+1:])
            dic[temp] = i
            ls.append(temp)

        temp = dic[min(ls)]
        nums = str(int(nums[:temp] + nums[temp+1:]))
        k-=1
    return nums

def removeKdigits (num: str, k: int) -> str:
    numStack = []

    # Construct a monotone increasing sequence of digits
    for digit in num:
        while k and numStack and numStack[-1] > digit:
            numStack.pop ()
            k -= 1

        numStack.append (digit)

    # - Trunk the remaining K digits at the end
    # - in the case k==0: return the entire list
    finalStack = numStack[:-k] if k else numStack

    # trip the leading zeros
    return "".join (finalStack).lstrip ('0') or "0"

print (solution ('1432219', 3))
print(removeKdigits('1432219',3))