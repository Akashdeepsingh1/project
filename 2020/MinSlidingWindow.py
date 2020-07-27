class Classy:
    def __init__(self):
        pass


    def minSlidingWindow(self,s,t):
        '''


        :param s:
        :param t:
        :return:
            Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

            Example:

            Input: S = "ADOBECODEBANC", T = "ABC"
            Output: "BANC"
        '''

        i = 0
        final_count = len(s)
        final_string = ""
        temp = len(t)
        t_ls = list(t)
        while i+len(t) < len(s):
            temp_string = s[i:i+temp]
            temp_ls = list(temp_string)
            flag = False
            for each in t_ls:
                if each not in temp_ls:
                    temp+=1
                    flag = True
                    break
            if not flag:
                temp_ln = len(temp_string)
                if final_count>temp_ln:
                    final_count = temp_ln
                    final_string = temp_string
                i+=1
        return final_count,final_string

S = "ADOBECODEBANC"
T = "ABC"


S1 ="a"
T1 = "b"



obj = Classy()
print (obj.minSlidingWindow (S1, T1))