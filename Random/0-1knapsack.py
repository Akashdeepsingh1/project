'''
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50


    60  100   120
10  60  60     60 
20  60 100    100
30  60 
40  60
50  60


'''


def knapsack(val, wt, w):
    if not val or not wt or not w or len(val) != len(wt):
        return None
