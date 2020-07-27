def levelOrder(root):

    l = []
    l_final = []
    node = []
    def recur(node):
        temp_ls = []
        while len(node)>0:
            temp = node.popleft()
            l.append(temp.val)
            if node.left:
                temp_ls.append(node.left)
            if node.right:
                temp_ls.append(node.right)
        l_final.append(l)
        node = temp_ls
        recur(node)
    recur(root)

    return l_final


