# # def mergeSort(nums):
# #
# #     if len(nums)>1:
# #         mid = len(nums)//2
# #         l = nums[:mid]
# #         r = nums[mid:]
# #
# #         mergeSort(l)
# #         mergeSort(r)
# #
# #         i = j = k = 0
# #
# #         while i<len(l) and j<len(r):
# #             if l[i]<r[j]:
# #                 nums[k] = l[i]
# #                 i+=1
# #             else:
# #                 nums[k] = r[j]
# #                 j+=1
# #             k+=1
# #
# #         while i<len(l):
# #             nums[k] = l[i]
# #             i+=1
# #             k+=1
# #
# #         while j<len(r):
# #             nums[k] = r[j]
# #             j+=1
# #             k+=1
# #
# #
# # def print_all(nums):
# #     for i in range(0, len(nums)):
# #         print(nums[i])
# #
# #
# #
# # arr = [12,11,13,5,6,7,33]
# # mergeSort(arr)
# #
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def mergeSort(nums):
#     le = len(nums)
#     if le>1:
#         mid = le//2
#         l = nums[:mid]
#         r = nums[mid:]
#
#         mergeSort(l)
#         mergeSort(r)
#
#         i = j = k = 0
#
#         while i < len(l) and j < len(r):
#             if l[i] < r[j]:
#                 nums[k] = l[i]
#                 i+=1
#
#             else:
#                 nums[k] = r[j]
#                 j+=1
#             k+=1
#
#         while i< len(l):
#             nums[k] = l[i]
#             k+=1
#             i+=1
#
#         while j<len(r):
#             nums[k] = r[j]
#             k+=1
#             j+=1
#
#
#

def mergeSort(nums,k):
    import heapq
    heapq.heapify(nums)
    print(heapq.nlargest(k, nums)[k-1])



arr = [12,11,13,5,6,7,33]
mergeSort(arr,4)

