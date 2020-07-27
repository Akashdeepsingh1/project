class classy:
    def __init__(self):
        self.refresh_list = set()

    def anagram(self, word, index,s):

        if len(word) == index and ''.join(word) in s:
            self.temp_list.append(''.join(word))
            self.visited.append(''.join(word))
            print(word)
        for i in range(index, len(word)):
            word[i],word[index] = word[index], word[i]
            self.anagram(word,index+1,s)
            word[i],word[index] = word[index], word[i]

    def groupAnagram(self, words):
        final_list = []
        self.visited = []
        for word in words:
            if word not in self.visited:
                self.temp_list = []
                self.anagram(list(word),0,words)
                final_list.append(self.temp_list)






obj = classy()
Input= ["eat", "tea", "tan", "ate", "nat", "bat"]
print (obj.groupAnagram(Input))