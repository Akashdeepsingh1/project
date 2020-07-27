class Stream:
    def __init__(self, stream):
        self.stream = stream.split()
        self.index = 0

    def next_word(self):
        self.index += 1
        return self.stream[self.index - 1]

    def end(self):
        return self.index == len(self.stream)

class TrieNode:
    def __init__(self):
        self.phrase = False
        self.words = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, phrase):
        current = self.root
        phrase = phrase.split()
        for word in phrase:
            if word not in current.words:
                current.words[word] = TrieNode()
            current = current.words[word]
        current.phrase = True

class Solution:
    def print_phrases(self, phrases, stream):
        trie = Trie()
        for p in phrases:
            trie.insert(p)
        trie_node = trie.root
        start_node = trie_node
        res = []
        while not stream.end():
            word = stream.next_word()
            if word in trie_node.words:
                trie_node = trie_node.words[word]
                res.append(word)
                if trie_node.phrase:
                    tmp = []
                    current = start_node
                    for w in res[1:]:
                        if w in current.words:
                            current = current.words[w]
                            tmp.append(w)
                            if current.phrase:
                                print(' '.join(tmp))
                                tmp = []
                                current = start_node
                    print(' '.join(res))
                    res = []
                    trie_node = start_node
            elif word not in trie_node.words:
                trie_node = start_node
                res = []

if __name__ == '__main__':
    so = Solution()
    phrases = ['a cat', 'through the grass', 'i saw a cat running']
    _stream = 'i was walking through the park and saw a cat running through the grass then i saw a cat running from the bushes'
    stream = Stream(_stream)
    so.print_phrases(phrases, stream)