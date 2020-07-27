def solution(s):
    l = len(s)
    if l<=2:
        return l
    else:
        final_sum = temp_sum = 2
        for i in range(2,l):
            if s[i] == s[i-1]:
                if s[i] == s[i-2]:
                    temp_sum = 2
                else:
                    temp_sum+=1
            else:
                temp_sum +=1
            if final_sum < temp_sum:
                final_sum = temp_sum

        return final_sum

print(solution('baaabbabbb'))
print(solution('abaaaa'))
