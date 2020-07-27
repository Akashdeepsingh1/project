def solution(s):
    l = len(s)
    if l<=2:
        return l
    else:
        final_sum = temp_sum = 2
        final_list = []
        temp_list = [s[0],s[1]]
        for i in range(2,l):
            if s[i] == s[i-1]:
                if s[i] == s[i-2]:
                    temp_sum = 2
                    temp_list= [s[i-1],s[i]]

                else:
                    temp_sum+=1
                    temp_list.append(s[i])
            else:
                temp_sum +=1
                temp_list.append(s[i])
            if final_sum < temp_sum:
                final_sum = temp_sum
                final_list = temp_list


        return ''.join(final_list)

print(solution('aabbaaabbabbb'))
print(solution('abaaaa'))
