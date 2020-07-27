from collections import defaultdict

class Solution:
    def suggestedProducts (self, products, searchWord):
        class TrieNode:
            def __init__ (self):
                self.children = defaultdict (TrieNode)
                self.suggestion = []

            def add_sugestion (self, product):
                if len (self.suggestion) < 3:
                    self.suggestion.append (product)

        products = sorted (products)
        root = TrieNode ()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_sugestion (p)

        result, node = [], root
        for char in searchWord:
            node = node.children[char]
            result.append (node.suggestion)
        return result


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

obj = Solution()
print (obj.suggestedProducts (products, searchWord))