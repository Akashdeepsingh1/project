class Classy:
    def __init__(self):
        pass

    def rotatedArray(self,arr,amount):
        '''

        :param arr:
        :param amount:
        :return:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
        Example 2:

        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1
        '''

        left_index = 0
        right_index = len(arr)-1

        def _find_element(left_index, right_index):
            if right_index <= left_index:
                return -1
            mid = (left_index + right_index)//2
            if arr[mid] == amount:
                return mid
            elif right_index - left_index == 1 and amount!=arr[right_index] and amount!=arr[left_index]:
                return -1
            elif mid-1>=0 and arr[mid-1] == amount:
                return mid-1
            elif mid+1<=len(nums)-1 and arr[mid+1] == amount:
                return mid+1
            if arr[left_index] <= amount <= arr[mid]:
                return _find_element(left_index,mid)
            elif arr[right_index]>= amount and amount>= arr[mid]:
                return _find_element(mid,right_index)
            elif arr[right_index]>=amount and arr[mid]>=amount:
                return _find_element(mid,right_index)
            elif arr[mid]<=amount and arr[left_index]>=amount:
                return _find_element(left_index,mid)
            else:
                return _find_element(left_index+1,right_index-1)


        return _find_element(left_index,right_index)

nums1 = [4,5,6,7,0,1,2]
nums = [7,6,5,4,2,1,0]
nums2 = [0,1,2,4,5,6,7]


obj = Classy()
print (obj.rotatedArray (nums, 0))
print (obj.rotatedArray (nums, 1))
print (obj.rotatedArray (nums, 2))
print (obj.rotatedArray (nums, 3))
print (obj.rotatedArray (nums, 4))
print (obj.rotatedArray (nums, 5))
print (obj.rotatedArray (nums, 6))
print (obj.rotatedArray (nums, 7))

t = 1
numt = [1]
print(obj.rotatedArray(numt,t))