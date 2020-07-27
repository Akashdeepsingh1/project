class Classy:
    def __init__(self):
        pass

    def longestPalindrome(self,s):
        le = len(s)
        if le == 0:
            return 0
        elif le == 1:
            return 1
        else:

            temp_matrix = [[0 for i in range(le)] for j in range(le)]

            # setting for i = 1
            count = 1
            start = 1
            for i in range(le):
                temp_matrix[i][i] = 1
                start  = s[i]

            k = 2
            while k<=le:

                for i in range(le-k+1):
                    temp = k + i - 1
                    if k == 2 and s[i] == s[i+1]:
                        temp_matrix[i][i+1] = 1
                        count = 2
                        start = i
                    elif s[i] == s[temp] and temp_matrix[i+1][temp-1] == 1:
                        if count < k:
                            count = k
                            start = i
                        temp_matrix[i][temp] = 1


                k+=1

            return s[start:start+count]

obj = Classy()
print (obj.longestPalindrome ('lbaace'))