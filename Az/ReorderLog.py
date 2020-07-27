def reorderLog(s):
    digit_ls = []
    word_ls = []

    for i in s:
        temp = i.split(' ')
        if temp[1].isdigit():
            digit_ls.append(i)
        else:
            word_ls.append(i)
    t = word_ls
    #word_ls.sort(key = lambda x: x.split(' ')[0])
    #t.sort(key=lambda x:x.split(' ')[0])
    t.sort(key=lambda x:x.split(' ')[0:])

    print(t+digit_ls)



    '''
        # sort by suffix first
        letterBackup.sort(key = lambda log: log.split()[0])
        
        # in case of same cases, sort by identifiers
        letterBackup.sort(key = lambda log: log.split()[1:])
        
        # combine letterLogs and digitLogs and return the final list
        return letterBackup + digBackup    
    '''

s =["dig1 8 1 5 1","dig2 3 6","let2 own kit dig","let3 art zero","let1 art can"]
s1 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

reorderLog(s1)


org0 = ['a2 act car', 'a8 act zoo', 'ab1 off key dog', 'g1 act car', 'a1 9 2 3 1', 'zo4 4 7']
org1 = ['g1 act car', 'a8 act zoo', 'a2 act car', 'ab1 off key dog', 'a1 9 2 3 1', 'zo4 4 7']
expected = ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]