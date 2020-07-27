def singleNumber (nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = 0
    for i in nums:
        a ^= i
    return a

def singleNumber2 (nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hash_table = {}
    for i in nums:
        try:
            hash_table.pop (i)
        except:
            hash_table[i] = 1
    return hash_table.popitem ()[0]

def findDuplicate (nums) -> int:
    dic = {}
    for i in nums:
        try:
            if i in dic.keys():
                return (i)
        except:
            dic[i] = 1


print(findDuplicate([1,3,4,2,2]))

#print(singleNumber2([4,1,2,1,2]))