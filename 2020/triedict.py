from collections import defaultdict


class Trie:

    def __init__ (self):
        """
        Initialize your data structure here.
        """
        self.trie = defaultdict (dict)

    def insert (self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.trie
        for ch in word:
            if ch not in temp.keys ():
                temp[ch] = {}
            temp = temp[ch]
        temp['*'] = True

    def search (self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.trie
        for ch in word:
            if ch not in temp:
                return False
            temp = temp[ch]
        if '*' in temp and temp['*']:
            return True
        else:
            return False

    def startsWith (self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.trie
        for ch in prefix:
            if ch not in temp:
                return False
            temp =temp[ch]
        return True




'''
["Trie","insert","search","search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]

'''

obj = Trie()
obj.insert('apple')
print (obj.search ('apple'))
print (obj.search ('app'))
print (obj.startsWith ('app'))
obj.insert('app')
print (obj.search ('app'))
