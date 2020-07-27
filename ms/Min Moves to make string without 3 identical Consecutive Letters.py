def solution(s):
    l = len(s)
    ls = list(s)
    if l <=2:
        return 0
    else:
        count = 0
        i = 0
        while i<l:
            temp_count = 1
            while i+1<l and s[i] == s[i+1]:
                temp_count +=1
                i+=1

            count += temp_count//3
            i+=1
        return count


print (solution ('baaaa'))
print(solution('baaabbaabbba'))