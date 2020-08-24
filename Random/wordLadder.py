'''

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
wordLadder(beginWord,endWord,wordList)

step 1 - create a dictionary with each word by changing a alphabet with an start
step 2 - take the start word and put star at  each alpha at a time 
and iterate over all its element with a count or step 
and see if the word matches in the dictionary with end word of not 

this is a bfs approach - so i would be using queue

'''


def worddict(wordList):
    if not wordList:
        return None
    dic = {}

    for word in wordList:
        for index in range(len(word)):
            temp_word = str(word[:index]) + '*' + str(word[index+1:])
            if temp_word in dic:
                dic[temp_word].append(word)
            else:
                dic[temp_word] = [word]
    return dic


def wordLadder(wordList, start, end):
    if not wordList or not start or not end:
        return None
    wordDictionary = worddict(wordList)

    queue = [(start, 0)]
    visited = set()

    while queue:
        word, step = queue[0]
        del queue[0]
        if word not in visited:
            for index in range(len(word)):
                temp_word = word[:index] + '*' + word[index+1:]
                if temp_word in wordDictionary:
                    for each in wordDictionary[temp_word]:
                        if each == end:
                            return step+1
                        queue.append((each, step+1))
            visited.add(word)
    return False


beginWord = "hit"
endWord = "hot"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(wordLadder(wordList, beginWord, endWord))
