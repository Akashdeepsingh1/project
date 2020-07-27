class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        min_val = prices[0]
        max_val = prices[0]
        min_index = 0
        max_index = 0
        final_sum = 0

        for i in range(1, len(prices)):
            if prices[i]< min_val:
                min_index = i
                min_val = prices[i]
            if prices[i]> max_val or min_index>max_index:
                max_index = i
                max_val = prices[i]
            if final_sum < (max_val - min_val) and min_index<max_index:
                final_sum = max_val - min_val

        return final_sum



n1 = [7,1,5,3,6,4, ]
n2 = [7,6,5,4,3,1]
obj = Solution()
print (obj.maxProfit (n1))
print (obj.maxProfit (n2))