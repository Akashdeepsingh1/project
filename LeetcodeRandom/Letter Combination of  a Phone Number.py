def letterCombinations ( digits: str):
    dic_alpha = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
                 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z'], 1: ['']}

    l = len (digits)
    i = -1
    temp =0
    temp_list = []
    while temp < l:
        if int(digits[temp])<1:
            temp_list = digits[temp:]
        else:
            temp_list = digits
            break


    def iterate(temp_list, i = 0):
        i += 1
        if len(temp_list)<0:
            return
        else:
            return temp_list[i] + ' ' + iterate(temp_list[i+1:])

    iterate(temp_list)




def iterate(nums, temp, final_list):
    if len(temp) == len(nums):
        final_list.append(temp)
    for i in dic_alpha[nums[index]]:
        temp.append(i)
        iterate(nums, temp+i,index+1,final_list)
        temp.pop(i)


letterCombinations("23")