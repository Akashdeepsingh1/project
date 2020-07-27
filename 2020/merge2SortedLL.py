class Classy:
    def __init__(self):
        self.ans = False
        self.finalword = ""
        self.tracking = []

    def _checkString(self,word):
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                return False
        return True

    def _permutation(self,word, index):
        if len(word)-1 == index:
            if self._checkString(word):
                self.ans =  True
                self.finalword = word[:]
        for i in range(index,len(word)):
            word[i],word[index] = word[index],word[i]

            self._permutation(word,index+1)
            word[i],word[index] = word[index],word[i]


    def notTogetherWords(self,s):
        self._permutation(list(s),0)
        return self.ans,''.join(self.finalword)



obj = Classy()
print (obj.notTogetherWords ('aabbccdde'))
