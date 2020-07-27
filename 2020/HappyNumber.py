class Classy:
    def __init__(self):
        pass

    def isHappy(self,n):
        self.dic = []

        while n not in self.dic:
            self.dic.append (n)
            temp_sum = 0
            while n >0:
                temp = n%10
                temp_sum += temp**2
                n //=10
            if temp_sum == 1:
                return True
            n = temp_sum

        return False

obj = Classy()
print (obj.isHappy(9))
