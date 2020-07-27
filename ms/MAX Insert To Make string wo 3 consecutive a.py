def solution(s):
    l = len(s)
    if l==0:
        return 2
    elif l == 1:
        if s == 'a':
            return 1
        else:
            return 4
    else:
        i = j = 0
        final_list = []
        while j<l:
            if j == 0 and s[j]!= 'a':
                final_list.extend(['a','a',s[j]])
                j+=1
            elif j-i >3:
                return -1
            elif j-i<=3 and s[j]!= 'a':
                temp = j-i
                if temp == 3 :
                    final_list.append(s[j])
                elif temp == 2:
                    if i == 0:
                        final_list.append(s[j])
                    else:
                        final_list.extend(['a',s[j]])
                elif temp == 1:
                    final_list.extend(['a','a',s[j]])
                i = j
                j +=1
            else:
                final_list.append(s[j])
                j+=1



        if final_list[-2] != 'a' or final_list[-1]!= 'a':
            if final_list[-1]!= 'a':
                final_list.extend(['a','a'])
            else:
                final_list.append('a')

        return final_list

print(''.join(solution('aabab')))
print(''.join(solution('aabaaba')))
print(''.join(solution('baba')))
print(''.join(solution('ababa')))
print(''.join(solution('aabaabaa')))
print(''.join(solution('baab')))
print(''.join(solution('aabbaa')))

print(''.join(solution('dog')))
print(''.join(solution('aa')))
print(solution('baaaa'))
#print(solution('abaaaa'))
