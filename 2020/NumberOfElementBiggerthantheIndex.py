def solution(nums):
    if len(nums) == 0:
        return []
    else:
        temp_matrix = [0] * len(nums)
        '''
         [2,1,3,4,1,2,1,5,4]
          0,1,2,3,4,5,6,7,8
                3,3,3,2,1,0,0,0,0
                   
        '''
        if nums[-1] >= len(nums)-1:
            temp_matrix[len(nums)-1] = 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= i:
                temp_matrix[i] = temp_matrix[i+1] + 1
            else:
                temp_matrix[i] = temp_matrix[i+1]




