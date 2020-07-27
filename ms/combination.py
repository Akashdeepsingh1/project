def solution(words):

    final_list = []

    def backtracking(words, l , r):
        if l==r:
            final_list.append(words[:])
            print(''.join(words[:]))
        for i in range(l,r):
            words[i], words[l] = words[l], words[i]
            backtracking(words,l+1,r)
            words[i], words[l] = words[l], words[i]


    backtracking(list(words), 0, len(words))

solution('abcd')