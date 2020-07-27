import LeetcodeRandom


def replaceQuestionMark(s):
    puzzle = list(s)
    alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(puzzle)):
        if puzzle[i] == "?":
            if i == 0:
                flag = True
                while flag:
                    ch = alpha_list[LeetcodeRandom.randrange(0, 25, 1)]
                    if i+1 < len([puzzle]):
                        if puzzle[i+1]!= ch:
                            puzzle[i] = ch
                            flag = False
                    else:
                        puzzle[i] = ch
                        flag = False
            elif i == len(puzzle)-1:
                flag = True
                while flag:
                    ch = alpha_list[LeetcodeRandom.randrange(0, 25, 1)]
                    if i-1>0:
                        if puzzle[i-1]!= ch :
                            puzzle[i] = ch
                            flag = False
                    else:
                        puzzle[i] = ch
                        flag = False
            else:
                flag = True
                while flag:
                    ch = alpha_list[LeetcodeRandom.randrange(0, 25, 1)]
                    if puzzle[i-1] != ch and puzzle[i+1]!= ch:
                        puzzle[i] = ch
                        flag = False
        else:
            continue


print (replaceQuestionMark ('xy?xz?'))