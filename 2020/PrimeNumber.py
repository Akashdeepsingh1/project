import math

def _check_primeNumber(n):
    sq_rt = int(math.sqrt(n))
    for i in range(2,sq_rt+1):
        if n%i == 0 :
            return False
    return True


def primeNumber(num1,num2):
    l = [False] * (num2-num1+1)
    count = 0
    for i in range(num1,num2+1):
        t = _check_primeNumber(i)
        if t:
            count+=1
            print(i)
    print(l,count)


print (primeNumber (1000,1200))
