import collections
class Solution:
    def minTransfers(self, transactions) -> int:
        # data structure
        trans,balance = collections.defaultdict(int),collections.defaultdict(list)
        for p1,p2,money in transactions:
            if p1 not in trans: trans[p1]=-money
            else: trans[p1]-=money
            if p2 not in trans: trans[p2]=money
            else: trans[p2]+=money
        re = 0
        notuse = []
        # to finish the first step and make an absolute pair transact
        for key,value in trans.items():
            if value==0: notuse.append(key)
            elif -value in balance:
                re+=1
                key2 = balance[-value].pop()
                notuse.append(key)
                notuse.append(key2)
            else:
                balance[value].append(key)
        # list the rest of value need to be transacted
        ls =  [v for k,v in trans.items() if k not in notuse]
        def backtrack(ls):
            if not ls: return 0
            if -ls[0] in ls:
                temp = ls[0]
                ls.remove(temp)
                ls.remove(-temp)
                return 1+backtrack(ls)
            else:
                res = float('inf')
                for i in range(1,len(ls)):
                    if ls[0]*ls[i]>0:continue
                    res = min(res,1+backtrack([ls[0]+ls[i]]+ls[i+1:]+ls[1:i]))
                return res
        return re+backtrack(ls) # backtracking to finish it

    def minTransaction(self, transaction):
        # create a dictionary with all the transactions
        self.tran = collections.defaultdict(int)
        for i,j,val in transaction:
            self.tran[j] -= val
            self.tran[i] += val

        self.balance = collections.defaultdict(list)

        count = 0
        removeNode = []
        for k,v in self.tran.items():
            if v == 0 :
                removeNode.append(k)
            elif -v in self.balance and len(self.balance[-v]) > 0 :
                count+=1
                removeNode.append(self.balance[-v].pop())
                removeNode.append(k)
                self.tran[k] = 0
            else:
                self.balance[v].append(k)


        remaining = [v for k,v in self.tran.items() if k not in removeNode ]



        def backtracking(ls):
            if not ls:
                return 0
            elif -ls[0] in ls:
                temp = -ls[0]
                ls.remove(temp)
                ls.remove(-temp)
                return 1+backtracking(ls)
            else:
                res = float('inf')
                for i in range(1,len(ls)):
                    if ls[0] *ls[i] >0:
                        continue
                    res = min(res,1+backtracking([ls[0]+ls[i]]+ ls[i+1:]+ls[1:i] ))
                    return res
        return backtracking(remaining)+count




t = [[0,1,10],[0,2,10],[3,5,10],[4,5,10],[2,1,5]]
obj = Solution()
print (obj.minTransfers (t))

'''A -> B 10
A -> C 10
D -> F 10
E -> F 10'''