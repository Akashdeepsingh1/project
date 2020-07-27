def maxProduct ( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_product= nums[0]
    current_product = 1
    l = 0
    while l<len(nums):
        current_product *= nums[l]
        if current_product> max_product:
            max_product = current_product
        if current_product <= 0:
            current_product = 1
        l+=1

    return max_product


print (maxProduct ([-2, 0, -1]))