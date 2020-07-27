class Node:
    def __init__ (self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.visited = {}
        if head is None:
            return None
        self.firstNode = None
        def helper(node):
            if node is None:
                return None
            if node in self.visited:
                return self.visited[node]
            self.visited[node] = Node(node.val,None,None)

            self.visited[node].next = helper(node.next)
            self.visited[node].random = helper(node.random)
            return self.visited[node]
        return helper(head)

        #return self.firstNode