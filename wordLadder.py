from collections import defaultdict, deque


def wordLadder(beginword,endword,wordList):
    d = defaultdict(list)
    for each in wordList:
        for i in range (len (each)):
            t = str (each[:i]) + '*' + str (each[i + 1:])
            d[t].append (each)

    que = deque()
    que.append((beginWord,1))
    visited = set()
    visited.add(beginWord)
    while que:
        word, count = que.popleft ()
        for i in range (len (word)):
            temp = str (word[:i]) + '*' + str (word[i + 1:])
            for each in d[temp]:

                if each == endword:
                    print (count)
                    break
                elif each not in visited:
                    que.append ((each, count + 1))
                    visited.add(each)


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
wordLadder(beginWord,endWord,wordList)