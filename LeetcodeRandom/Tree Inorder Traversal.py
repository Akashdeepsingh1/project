
        res, stack = [], []
		while root or stack:
			if root:
				stack.append(root)
				root = root.left
			else:
				node = stack.pop()
				res.append(node.val)
				root = node.right
		return res

