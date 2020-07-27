'''

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

'''

from collections import defaultdict
import random
class Trie:
    def __init__(self):
        self.word = defaultdict()
        self.phase = False
        self.suggestion = set()
        self.count = random.randint(0,10)

class Classy:

    def __init__(self):
        self.head = Trie()

    def insert(self, phases):
        if not phases: return 0

        for each in phases:
            temp_dic = self.head
            for ch in each:
                if ch not in temp_dic.word:
                    temp_dic.word[ch] = Trie()
                temp_dic.suggestion.add((each, temp_dic.count))
                temp_dic = temp_dic.word[ch]
            temp_dic.word['phase'] = True

    def searchWord(self, phases, word):
        if not phases or not word:
            return 0
        self.insert(phases)
        temp_dic = self.head
        for each in word:
            if each in temp_dic.word:
                suggest = list(temp_dic.suggestion)
                suggest.sort()
                if len(suggest) > 3:
                    print(suggest[:3])
                else:
                    print(suggest)
                temp_dic = temp_dic.word[each]
            else:
                print([])


obj = Classy()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

obj.searchWord(products,searchWord)