def solution(s):
    final_list = []
    for i in range(len(s)):
        if i <= 1:
            final_list.append(s[i])
        else:
            if final_list[-1] != s[i]:
                final_list.append(s[i])
            else:
                if final_list[-2] !=  s[i]:
                    final_list.append(s[i])

    return ''.join(final_list)


print (solution ('xxxxtxxxx'))
print(solution('eaadaaad'))
print(solution('uuuuuxaaaaaxuuu'))