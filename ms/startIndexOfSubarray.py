def subarrayIndex(a, b ):
    for i in range(len(a)):
        count = 0
        if a[i] == b[0]:
            for j in range(len(b)):
                if a[i+j] == b[j]:
                    count +=1
                else:
                    break
            if count == len(b):
                return i
    return -1


a = [1,2,4,4,4,4,4,4,4,4,4,4,7,8]
b = [4,5]
print (subarrayIndex (a, b))