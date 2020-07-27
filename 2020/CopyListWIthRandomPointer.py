class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.random = None


def copyRandomList(self,head):
    if head is None:
        return None
    self.visited = {}

    def helper(self,node):
        if node is None:
            return None
        if node in self.visited:
            return self.visited[node]
        self.visited[node] = Node(node.val)
        self.visited[node].next = self.helper(node.next)
        self.visited[node].random = self.helper(node.random)
        return self.visited[node]

    return self.helper(head)
