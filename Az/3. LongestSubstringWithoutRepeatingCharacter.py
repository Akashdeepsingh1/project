def lengthOfLongestSubtring(s):
    l = list(s)
    max_count = 0
    for i in range(len(l)):
        temp_count = 1
        temp_list = [l[i]]
        for j in range(i+1,len(l)):
            if l[j] not in temp_list:
                temp_list.append(l[j])
                temp_count+=1
            else:
                break
        if temp_count>max_count:
            max_count = temp_count
            final_list = temp_list

    return max_count


s = 'abcabcbb'
s1 = 'bbbbbbb'
s2 = 'pwwkew'
s3 = "tmmzuxt"
s4 = 'bbtablud'
#print (lengthOfLongestSubtring (s1))


def lengthOfLongestSubstring2(s):
    dic_loc = {}
    start = 0
    max_count = 0
    ls = list(s)
    count = 0
    l = len(ls)

    for i in range(l):
        if ls[i] in dic_loc:
            if dic_loc[ls[i]] >= start:
                start = dic_loc[ls[i]] +1
                count -= dic_loc[ls[i]]
                dic_loc[ls[i]] = i
        else:
            dic_loc[ls[i]] = i
        count += 1

        if count>max_count:
            max_count = count
    return max_count-1


print (lengthOfLongestSubstring2 (s1))