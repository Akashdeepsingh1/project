# merging the two trees

class Node:
    def __init__(self,val):
        self.val  = val
        self.left = None
        self.right = None


def merge2Trees(a, b):
    if a is None:
        return b
    if b is None:
        return a
    a.val = a.val + b.val
    a.left = merge2Trees(a.left,b.left)
    a.right = merge2Trees(a.right,b.right)
    return a

def merge2Trees2(a,b):
    '''
    :param a:  root a
    :param b: root b
    :return: merge tree
    '''

    if not a and not b:
        return None

    if not a and b:
        return b
    if not b and a:
        return a

    a.val += b.val

    a.left = merge2Trees2(a.left,b.left)
    a.right = merge2Trees2(a.right,b.right)

    return a



def print_node(node):
    if node is None:
        return
    print(node.val)
    if node.left is not None:
        print_node(node.left)
    if node.right is not None:
        print_node(node.right)

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)

b1 = Node(1)
b2 = Node(2)
b3 = Node(3)
b4 = Node(4)
b5 = Node(5)

a1.left = a2
a1.right = a3
a2.left = a4
a3.left = a5

b1.left = b2
b1.right = b4
b2.right = b3
b3.right = b5


node = merge2Trees(a1,b1)
print_node(node)

