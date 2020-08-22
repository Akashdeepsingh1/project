def reverseString(sentence):
    # error checking
    if not sentence:
        return ""
    temp_sentence_list = list(sentence)
    start = 0
    end = len(temp_sentence_list)
    '''
    h,e,l,l,o, ,a , ,w,o,r,l,d,y 
    
    
    '''
    for ind in range(end//2):
        temp_sentence_list[ind], temp_sentence_list[end-ind -
                                                    1] = temp_sentence_list[end-ind-1], temp_sentence_list[ind]

    # [y,d,l,r,o,w, , a, , o, l, l, e, h]

    end = 0
    for ind in range(len(temp_sentence_list)):
        if temp_sentence_list[ind] == " ":

            # reverse the word using 2 pointer
            if end-start >= 2:
                count = 0
                while start+count < end-count:
                    temp_sentence_list[start+count], temp_sentence_list[end-count-1
                                                                        ] = temp_sentence_list[end-count-1], temp_sentence_list[start+count]
                    count += 1

            start = ind+1
            end = ind+1

        else:
            end += 1
    for ind in range(start, (end+start)//2):
        temp_sentence_list[start], temp_sentence_list[end -
                                                      1] = temp_sentence_list[end-1], temp_sentence_list[start]

    return "".join(temp_sentence_list)


'''
testcase 1
    [h,e,l,l,o, ,a , ,w,o,r,l,d,y] 
    
    [y,d,l,r,o,w, , a, , o, l, l, e, h]
    
    start = 0 
    end = 0, 1, 2, 3, 4, 5, 6, 
    [w,o,r,l,d,y, 
    
testcase1 

    [a,b,c, ,h,g, , d,e,f]
    
    [f,e,d, ,g,h,  , c,b,a]
    
    start = 0 

    
'''


#print(reverseString("hello world"))
print(reverseString("abc def"))
