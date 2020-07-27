def sum3(nums):

    l = len(nums)
    s= []
    if l>2:
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    if nums[i]+nums[j]+nums[k] == 0:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        if temp not in s:
                            s.append(temp)


    temp = set(s)
    return s




def threesum(nums):
    l = []
    for i in range(0, len(nums)-1):
        ls = []
        for j in range(i+1, len(nums)):
            temp = nums[i] + nums[j]
            if -temp in ls:
                temp_ls = [nums[i],nums[j],-temp]
                temp_ls.sort()
                if temp_ls not in l:
                    l.append(temp_ls)
            else:
                ls.append(nums[j])
    return l



def threesum2(nums):
    dic = {}
    def twosum(nums):
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                temp = nums[i]+nums[j]
                if temp not in dic:
                    if nums[i]< nums[j]:
                        dic[nums[i] + nums[j]] = [[nums[i],nums[j]]]
                    else:
                        dic[nums[i] + nums[j]] = [[nums[j], nums[i]]]
                else:
                    temp_l =[]
                    
                    temp_l = dic[nums[i]+nums[j]]
                    temp_l.append([nums[i],nums[j]])
                    dic[nums[i]+nums[j]] = temp_l

    twosum(nums)
    l = []
    for i in range(0, len(nums)):
        if -nums[i] in dic:
            le = len(dic[-nums[i]])
            while le >=1:
                val0, val1 = dic[-nums[i]][le]
                if i != val0 and i != val1:
                    temp = -nums[i]
                    temp1 = []
                    if nums[val0] <= nums[val1] and nums[val0] <= -temp:
                        if nums[val1] <= -temp:
                            temp1.append([val0,val1,-temp])

                    elif nums[val1] <= nums[val0] and nums[val1] <= -temp:
                        if nums[val0] <= -temp:
                            temp1.append([val1,val0,-temp])

                    else:
                        if nums[val1]< nums[val0]:
                            temp1.append([-temp,val1,val0])
                        else:
                            temp1.append([-temp,val0,val1])

                    if len(temp1)>2 and  temp1 not in l:
                        l.append(temp1)
                le-=1


# def threeSum (self, nums: List[int]) -> List[List[int]]:
#     l = len (nums)
#     nums.sort ()
#     ls = []
#
#     for i in range (l):
#         s = i + 1
#         lst = l - 1
#         while s < lst:
#             temp = nums[i] + nums[s] + nums[lst]
#             if temp == 0:
#                 ls.append (nums[i] + nums[s] + nums[lst])
#                 s += 1
#                 lst -= 1
#
#             elif temp < 0:
#                 s += 1
#             else:
#                 lst -= 1
#     return ls


#l=sum3([-1, 0, 1, 2, -1, -4])

print(threesum2([-1,0,1,2,-1,-4]))

