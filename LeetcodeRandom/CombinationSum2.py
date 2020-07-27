def combinationSum(candidates, target):
    final_list =[]



    def combi(nums_sum, nums_list, input_list, target):
        for i in range(len(input_list)):
            if nums_sum  + input_list[i] == target:
                final_list.append(nums_list+[input_list[i]])


            if nums_sum + input_list[i] > target:
                return

            combi(nums_sum+input_list[i], nums_list + [input_list[i]], input_list[i:], target)
    combi(0,[],candidates,target)

    print(final_list)

combinationSum([2,3,5,7],7)