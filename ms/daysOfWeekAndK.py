def solution(s,k):
    week = ['mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','sun']
    temp = k%7
    i = 0
    while i<7:
        if week[i] == s:
            break
        else:
            i+=1

    return week[i+temp]

print(solution('sat',23))
print(solution('wed',2))
