class Solution:
    def myAtoi (str: str) -> int:
        str = str.strip ()
        last = 0
        for each in str:
            if each in ['1','2','3','4','5','6','7','8','9','0','-','.']:
            #if (data > 47 and data < 58) or data == 45 or data == 46 :
                flag = True
                last+=1
            else:
                break
        if flag:
            data= int(str[0:last+1])
            if data > 2**31:
                return 2**31
            elif data < -2 ** 31:
                return -2**31
            else:
                return data
        else:
            return 0
    if __name__ == '__main__':
        print (myAtoi (' -555 Hello ------    World   45'))










