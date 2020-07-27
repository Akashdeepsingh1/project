def maxProfit( prices):
    profit = 0
    flag = True
    l = len(prices)
    start = 0
    for i in range(0,l):
        if  i< l-1 and flag:
            if prices[i]>=prices[i+1]:
                #start = prices[i+1]
                #i = i+1
                pass
            else:
                start = prices[i]
                flag = False

        elif i< l -1:
            if prices[i]> prices[i+1]:

                if prices[i]>start:
                    profit = profit + (prices[i] - start)
                    flag = True
            elif prices[i] < prices[i+1]:
                pass
        elif prices[i] > start and flag == False:
            profit = profit + (prices[i] - start)


    return profit

# print(maxProfit([7,1,5,3,6,4]))
# print(maxProfit([1,2,3,4,5]))
# print(maxProfit([7,6,4,3,1]))
print(maxProfit([8,6,4,3,3,2,3,5,8,3,8,2,6]))