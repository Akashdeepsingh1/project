def solution(word):
    final_list = []
    def helper(index):
        if index == len(word):
            final_list.append(''.join(word))
            print(''.join(word))
        for i in range(index, len(word)):
            word[i], word[index] = word[index], word[i]
            helper(index+1)
            word[i], word[index] = word[index], word[i]

    helper(0)

solution(list('eat'))