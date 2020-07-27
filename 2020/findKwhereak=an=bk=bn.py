class Classy:
    def __init__(self):
        pass

    def findK(self,a,b):
        sum_a = sum(a)
        sum_b = sum(b)

        if sum_a!= sum_b:
            return 0
        curr_a = curr_b = 0
        res = 0
        for i in range(len(a)-1):
            curr_a += a[i]
            curr_b += b[i]
            sum_a -= a[i]
            sum_b -= b[i]
            if curr_a == curr_b == sum_a == sum_b:
                res +=1
        return res

obj = Classy()
A = [4,-1,0,3]
B = [-2,5,0,3]
print (obj.findK (A, B))
A1 = [2,-2,-3,3]
B1 = [0,0,4,-4]
print(obj.findK(A1,B1))
A3 = [4,-1,0,3]
B3 = [-2,6,0,4]
print(obj.findK(A3,B3))
A4 = [3,2,6]
B4 = [4,1,6]
print(obj.findK(A4,B4))
A5 = [1,4,2,-2,5]
B5 = [7,-2,-2,2,5]
print(obj.findK(A5,B5))