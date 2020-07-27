class Classy:
    def __init__(self):
        pass

    def cropWords(self,sentence,k):
        '''

        :param sentence: Codility Me test coders
        :param k: 14
        :return: Codility Me
        '''
        temp_ls = sentence.split(' ')
        final_str = ""
        index = 0
        while k >0:
            k -= len(temp_ls[index])
            if k >=0:
                final_str += temp_ls[index]
                final_str += " "
                k-=1
            index+=1
        return final_str.rstrip(' ')


obj = Classy()
sentence = "Codility Me a test coders"
k = 14
print (obj.cropWords (sentence, k))