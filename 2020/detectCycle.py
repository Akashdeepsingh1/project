
from collections import defaultdict
class Cyclic:
    def __init__(self):
        self.graph = defaultdict(list)

# to do





class Scheduling:
    def __init__(self):
        pass


    def sche(self, intervals):
        intervals.sort(key = lambda i:i[0])
        import heapq

        l = []
        heapq.heappush(l,intervals[0][1])

        for i in range(1,len(intervals)):
            temp = heapq.heappop(l)
            if temp >= intervals[i][0]:
                heapq.heappush(l,temp)
                heapq.heappush(l,intervals[i][1])
            else:
                heapq.heappush(l,intervals[i][1])

        return l

    def rob (self, nums) -> int:
        if not nums:
            return 0
        dp = [0] * len (nums)
        max_val = 0
        for i in range (2, len (nums)):
            if i == 2:
                dp[i] = nums[i] + nums[i - 2]

            else:
                dp[i] = nums[i] + max (dp[i - 2], dp[i - 3])
            if dp[i]>max_val:
                max_val = dp[i]
        return max_val


t = [(0, 10), (9, 12), (5, 9), (11, 15)]
obj = Scheduling()
print (obj.sche (t))

t1 = [1,2,3,1]
t2 = [2,7,9,3,1]
print (obj.rob (t2))




'''

    def isCyclic(self, currCourse, courseDict, checked, path):
        """   """
        # 1). bottom-cases
        if checked[currCourse]:
            # this node has been checked, no cycle would be formed with this node.
            return False
        if path[currCourse]:
            # came across a marked node in the path, cyclic !
            return True

        # 2). postorder DFS on the children nodes
        # mark the node in the path
        path[currCourse] = True

        ret = False
        # postorder DFS, to visit all its children first.
        for child in courseDict[currCourse]:
            ret = self.isCyclic(child, courseDict, checked, path)
            if ret: break

        # 3). after the visits of children, we come back to process the node itself
        # remove the node from the path
        path[currCourse] = False

        # Now that we've visited the nodes in the downstream,
        #   we complete the check of this node.
        checked[currCourse] = True
        return ret


'''