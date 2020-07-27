from collections import defaultdict, Counter

class Classy:
    def __init__(self):
        pass


    def minSubStringWindow(self,t,s) -> int :
        if not s or not t:
            return 0

        s_counter = Counter(s)
        len_counter = len(s_counter)
        end = start = 0
        final_len = float('inf')

        while end< len(t):
            if t[end] in s_counter:
                s_counter[t[end]] -= 1
                if s_counter[t[end]] == 0:
                    len_counter -=1



            while len_counter == 0:
                if t[start] in s_counter:
                    s_counter[t[start]] += 1
                    len_counter +=1
                start+=1

                if end-start < final_len:
                    final_len = end - start
            end += 1

        return final_len

    def longestSubStringWithoutRepeatingChara(self,S):
        start = end = 0
        counter_dic = defaultdict(int)
        counter = 0
        final_len = float('-inf')
        while end<len(S):
            counter_dic[S[end]]+=1
            if counter_dic[S[end]] > 1:
                counter +=1

            while counter != 0:
                counter_dic[S[start]]-=1
                if counter_dic[S[start]] == 0:
                    counter -= 1
                start+=1


            if counter == 0 :
                if final_len< end - start:
                    if start == 0:
                        final_len = end  - start + 1
                    else:
                        final_len = end - start
            end+=1
        return final_len

    def stringWithMaxkDistinctCharacter(self,s,k):
        start = end = 0
        counter_dic = defaultdict(int)
        unique_char = 0
        final_len = float('-inf')
        while end < len (s):
            counter_dic[s[end]] +=1
            if counter_dic[s[end]] == 1:
                unique_char +=1

            if unique_char == 2:
                if final_len < end - start:
                    if start ==0 :
                        final_len = end - start + 1
                    else:
                        final_len = end - start

            while unique_char > 2:
                counter_dic[s[start]] -= 1
                if counter_dic[s[start]] == 1:
                    unique_char -= 1
                start+=1


            end +=1

obj = Classy()
print (obj.minSubStringWindow ('ADOBECODEBANC', 'ABC'))

print(obj.longestSubStringWithoutRepeatingChara('abcabcbb'))
print(obj.longestSubStringWithoutRepeatingChara('bbbbb'))
print(obj.longestSubStringWithoutRepeatingChara('pwwkew'))