def solution(s):
    dic_alpha = {}
    dic_num = {0:0}
    l = list(s)
    for each in l:
        if each in dic_alpha:
            temp = dic_alpha[each]
            dic_alpha[each]+=1

            if temp+1 in dic_num:
                dic_num[temp+1] +=1
            else:
                dic_num[temp+1] = 1
            if temp != 0:
                dic_num[temp] -= 1
        else:
            dic_alpha[each] = 1
            dic_num[1] = 1

    FLAG = True
    while FLAG:
        FLAG2 = False
        for k,v in enumerate(dic_num):
            #see if there is any key with more than 1 value
            if v >= 2:
                FLAG2 = True
                for k1,v1 in enumerate(dic_alpha):
                    if k1 == v:
                        dic_alpha[k1]-=1
                        dic_num[k1]-=1
                        if k1-1 in dic_num:
                            dic_num[k1-1] += 1
                        else:
                            dic_num[k1-1] = 1
            #if it is found then find a corresponding alphabet and -1 from it and update dic_num
        if not FLAG2:
            FLAG = False
            break




    print(dic_num)
    print(dic_alpha)

solution('eeeefffff')