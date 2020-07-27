def solution(s, n):
    print(len(s))
    l = s.split(' ')
    final_list = []
    for each in l:
        if len(each) <= n:
            final_list.append(each)
            n-=(len(each)+1)
        else:
            break

    return ' '.join(final_list)


print (solution ("The quick brown fox jumps over the lazy dog", 39))
print(solution('Codility We test coders',14))
print(solution('Why not',39))
