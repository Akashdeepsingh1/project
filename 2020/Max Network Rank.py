class Classy:
    def __init__(self):
        pass

    def maxRank(self,A,B):
        from collections import defaultdict
        self.dic = defaultdict(list)
        for i in range(len(A)):
            self.dic[A[i]].append(B[i])
            self.dic[B[i]].append(A[i])

        max_network = 0
        final_node = (0,0)
        for k,v in self.dic.items():
            temp_sum = len(v)
            for each in v:
                temp_val = len(self.dic[each])
                if temp_val+temp_sum-1>=max_network:
                    if (k,each) != final_node and (each,k)!=final_node:
                        max_network = temp_val+temp_sum-1
                        final_node = (k,each)

        return max_network,final_node

obj = Classy()
A = [1,2,3,3]
B = [2,3,1,4]
print (obj.maxRank (A, B))
