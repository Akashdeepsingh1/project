import math

def atoi(s:str):
    st = s.strip()
    st_ls = st.split(' ')
    if st_ls is not None:
        obj = st_ls[0]
        flag = False
        temp_num = 0
        for i in range(len(obj)):
            temp = ord(obj[i])
            if i == 0 and temp == 45:
                flag = True
            if 48<=temp<=57 and i != 0:
                temp_num = temp_num * 10 + obj[i]
            elif i!= 0 :
                break


        if temp_num != 0:
            if flag:
                temp_num *= -1
            if temp_num < -2147483648:
                return -2147483648
            elif temp_num > 2147483648:
                return 2147483648
            else:
                return temp_num

s = '               -91283472332              dsfadsfa           adfasd'
print (atoi (s))
