
from collections import defaultdict

class Classy:
    def __init__(self):
        pass

    class Dictionary:
        def __init__(self):
            self.trie = defaultdict(dict)

        def createTrie(self,product):
            for word in product:
                temp = self.trie
                for cha in word:
                    if cha in temp:
                         temp = temp[cha]
                    else:
                        temp[cha] = {}
                temp['*'] = True

            return self.trie

    def searchSuggestion(self, product, searchWord):
        '''

        :param words:
        :param searchWord:
        :return:

        Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

        Return list of lists of the suggested products after each character of searchWord is typed.



        Example 1:

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
        Example 2:

        Input: products = ["havana"], searchWord = "havana"
        Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
        Example 3:

        Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
        Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
        Example 4:

        Input: products = ["havana"], searchWord = "tatiana"
        Output: [[],[],[],[],[],[],[]]

        '''

        product.sort()

        t = self.Dictionary()
        trie = t.createTrie(product)
        curr = trie
        final_list = []

        for each in searchWord:

            test = curr[each]

            for k,v in test.items():
                if '*' in v:
                    print('True')
                if k in test:
                    test = test[k]
            if 'True' in v:
                print('True')
            curr = curr[each]





obj = Classy()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
obj.searchSuggestion(products,searchWord)



