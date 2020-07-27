class solution:
    def __init__(self):
        self.head = {}

    def set(self,word):
        curr = self.head
        for each in word:
            if each in curr:
                curr = curr[each]
            else:
                curr[each] = {}
                curr = curr[each]

        curr['*'] = True


    def get(self, word):
        curr = self.head
        for each in word:
            if each in curr:
                curr = curr[each]
            else:
                return False
        if '*' in curr:
            return True
        else:
            return False

obj = solution()
obj.set('hary')
obj.set('harry')
obj.get('tom')
obj.set('tom')
print (obj.get ('harry'))