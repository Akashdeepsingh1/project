from collections import defaultdict

class Classy:
    def __init__(self):
        self.head = defaultdict()


    def createTrie(self, phases):
        if not phases: return 0

        for word in phases:
            temp = self.head
            for each in word.split():
                if each not in temp:
                    temp[each] = {}
                temp = temp[each]
            temp['phase'] = True


    def searchWord(self,phrase, stream):
        if not phrase: return 0

        self.createTrie(phrase)

        ls_word = stream.split()
        temp_ds = self.head
        i = 0
        rs = []
        while i < len(ls_word):
            if ls_word[i] in temp_ds:
                rs.append(ls_word[i])
                temp_ds = temp_ds[ls_word[i]]


                if 'phase' in temp_ds:
                    temp_head = self.head
                    rs_temp = []
                    for temp_word in rs[1:]:
                        if temp_word in temp_head:
                            temp_head = temp_head[temp_word]
                            rs_temp.append (temp_word)
                            if 'phase' in temp_head and temp_head['phase']:
                                print (' '.join (rs_temp))
                        else:
                            rs_temp = []
                            temp_head = self.head
                    print(' '.join(rs))
                    rs = []

            else:
                rs =[]
                temp_ds = self.head
            i+=1





phrases = ['a cat', 'through the grass', 'i saw a cat running']
_stream = 'i was walking through the park and saw a cat running through the grass then i saw a cat running from the bushes'

obj = Classy()
print (obj.searchWord (phrases, _stream))
