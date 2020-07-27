class Classy:
    def __init__(self):
        pass


    def maxSubarry(self, n):
        '''

        :param n:  [-2,1,-3,4,-1,2,1,-5,4],
        :return: 6
        '''

        le = len(n)
        if le ==0:
            return 0
        elif le ==1:
            return n[0]
        else:

            max_sum = n[0]
            current_sum = n[0]

            for i in range(1,le):
                current_sum += n[i]
                current_sum = max(n[i], current_sum)
                max_sum = max(max_sum,current_sum,n[i])

            return max_sum

obj = Classy()
test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test2 = [8,-19,5,-4,20]
test3 = [-1]
test4 = [-1,-2]
test5 = [-1,0]
print (obj.maxSubarry (test4))

