class Classy:
    def __init__(self):
        pass

    def productExceptSelf(self, nums):
        self.temp1 = [1]*len(nums)
        self.temp2 = [1]*len(nums)

        for i in range(len(nums)-1):
            self.temp1[i+1] = self.temp1[i] * nums[i]
            print(self.temp1[i+1])

        for i in range(len(nums)-1,0,-1):
            self.temp2[i-1] = self.temp2[i] * nums[i]
            print(self.temp2[i-1])



obj = Classy()
print (obj.productExceptSelf ([4, 5, 1, 8, 2]))







