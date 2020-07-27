class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None




def helper(s,t):
    if s is None and t is None:
        return True
    elif s is None or t is None or s.val != t.val:
        return False
    elif s.val == t.val:
        return helper(s.left,t.left) and helper(s.right,t.right)
    else:
        return False


def isSubtree(s,t):
    if s is None and t is None:
        return True
    elif s is None or t is None or s.val != t.val:
        return False
    elif s.val == t.val:
        if helper (s, t):
            return True
    return isSubtree(s.left,t) or isSubtree(s.right,t)
