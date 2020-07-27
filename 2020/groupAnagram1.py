class Anagram:
    def __init__ (self):
        self.ans = []
        self.temp_ans = []

    def _permutation (self, word, index):
        '''
        @param: str - take a word and find all its permutation and check if exist in self.wordList
        @return: list
        '''
        if len (word)-1 == index:
            temp_word = str(''.join(word))
            if temp_word in self.wordList:
                self.temp_ans.append (temp_word[:])
                self.wordList[self.wordList.index (temp_word)] = '-1'

        for i in range (index, len (word)):
            word[i], word[index] = word[index], word[i]
            self._permutation (word, index + 1)
            word[i], word[index] = word[index], word[i]

    def checkAnagram (self, wordList):
        '''
            @param wordList []: List -  wordlist contains the word and we need to find if anagram each word exist in the list
            @return [[]]: list - list of list of each anagram that are same
            @exception: if the list is empty or wrong input

            logic - take each word and find all its permutation and see it exist in the list and it exist remove add the common word and make that -1 in the list.

        '''
        self.wordList = wordList
        for each in wordList:
            if each != '-1':
                self.temp_ans = []
                self._permutation (list (each), 0)
                self.ans.append(self.temp_ans[:])

        return self.ans


'''
["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
'''
wordlist = ["eat", "tea", "tan", "ate", "nat", "bat"]
wort_temp = wordlist

wort_temp.sort(key= lambda i:i in i[:])
obj = Anagram()
print (obj.checkAnagram (wordlist))