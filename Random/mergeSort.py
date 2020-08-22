def mergeSort(nums):
    if not nums or len(nums) <= 1:
        return
    mid = len(nums)//2
    l = nums[mid:]
    r = nums[:mid]
    mergeSort(l)
    mergeSort(r)

    i = j = k = 0

    while i < len(l) and j < len(r):
        if l[i] > r[j]:
            nums[k] = r[j]
            j += 1
        else:
            nums[k] = l[i]
            i += 1
        k += 1
    while i < len(l):
        nums[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        nums[k] = r[j]
        j += 1
        k += 1
    return nums


nums = [12, 7, 3, 8, 0, 1, 2, -1]
print(mergeSort(nums))
