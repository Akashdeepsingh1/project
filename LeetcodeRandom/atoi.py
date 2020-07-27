class Solution:
    def myAtoi( str: str) -> int:
        str = str.strip()
        data = ord(str[0])
        if (data > 47 and data < 58 ) or data == 45:
            flag = False
            if data == 45:
                flag = True
                sums = 0
            else:
                sums = str[0]
                print(sums)
            sums = int(sums)
            for each in range(1,len(str)):
                if ord(str[each]) == 32:
                    break
                else:
                    sums = sums*10 + int(str[each])
            if sums > 2**31:
                if flag:
                    return -1 * 2**31
                else:
                    return 2**31
            else:
                if flag:
                    return sums * -1
                else:
                    return sums
        else:
            return 0


    if __name__ =='__main__':
        print(myAtoi( ' -555 Hello ------    World   45'))










    