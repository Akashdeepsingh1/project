
def _checkPalindrome(st):
    for i in range(len(st)//2):
       if st[i] != st[len(st)-i-1]:
           return False
    return True


def longestPalindrome(st):
    final_count = 0
    final_word = ""
    '''
    babad
    
    '''
    visited = set()

    if _checkPalindrome(st):
        return len(st),st
    else:
        for i in range(len(st)-1):
            for j in range(i+1,len(st)):
                temp = st[i:j]
                if temp not in visited:
                    if _checkPalindrome(temp):
                        if len(temp)>final_count:
                            final_count = len(temp)
                            final_word = temp
                    visited.add(temp)

        return final_count,final_word



def longestPalindrome1(st):
    '''

    :param st:
    :return:

        b   a   b   a   d
    b   1   0   3   0   0
    a       1   0   3   0
    b           1   0   0
    a               1   0
    d                   1


        b   a   d    a   b
    b   1   0       0   5
    a       1   0   3   0
    d           1   0
    a               1   0
    b                   1





    '''


    final_count = 0
    final_word = ""
    l = len(st)
    mat  = [[0 for i in range(l)] for j in range(l)]

    for i in range(l):
        mat[i][i] = 1

    for i in range(l-1):
        if st[i] == st[i+1]:
            mat[i][i+1]= 2

    for i in range(2,l-1):

        for j in range(l-i+1):
            if st[j] == st[i+j] and mat[i+1][j-1]:
                mat[j][i+j] = mat[i+1][j-1] + 2
                if mat[j][i+j] > final_count:
                    final_count = mat[j][i+j]
                    final_word = st[i:i+final_count]

    return final_count,final_word



print (longestPalindrome1 ('babad'))