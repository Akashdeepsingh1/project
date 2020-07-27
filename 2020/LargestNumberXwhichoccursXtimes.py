class Classy:
    def __init__(self):
        pass

    def countX(self, val_list):
        if not val_list:
            return -1
        from collections import defaultdict

        dic = defaultdict(int)
        for each in val_list:
            dic[each]+=1

        final_val  = -1
        for k,v in dic.items():
            if k == v and final_val < k:
                final_val = k
        return final_val


obj = Classy()
A = [3,8,2,3,3,2]
B = [7,1,2,8,2]
C = [3,1,4,1,5]
print (obj.countX (A))
print(obj.countX(B))
print(obj.countX(C))
