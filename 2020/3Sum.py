class Classy:
    def __init__(self):
        pass

    def _helper(self,s):
        self.two_sum = {}

        for i in range(len(s)):
            for j in range(i+1,len(s)):
                temp = s[i]+s[j]
                if temp not in self.two_sum:
                    self.two_sum[temp] = [[s[i],s[j]]]
                else:
                    check_value = self.two_sum[temp]
                    if [s[i],s[j]] not in check_value and [s[j],s[i]] not in check_value:
                        check_value.append([s[i],s[j]])
                        self.two_sum[temp] = check_value



    def threeSum(self, s):
        s.sort()
        self._helper(s)
        s = set()

        for each in s:
            temp = -1 * each
            if temp in self.two_sum:
                for i in each:
                    temp1, temp2 = i
                    if ([temp,temp1,temp2] not in s) and ([temp1,temp,temp2] not in s) and ([temp1,temp2,temp] not in s) and ([temp2, temp, temp1] not in s) and ([temp2,temp1,temp] not in s) and ([temp,temp2,temp1] not in s):
                        s.add([temp,temp1,temp2])

        return s

obj = Classy()
print (obj.threeSum ([-1, 0, 1, 2, -1, -4]))


