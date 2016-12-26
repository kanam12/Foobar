def tree(h, q):
	if h == 1:
		return [-1]
	p = [-1] * len(q)
	root = (2**h) - 1
	nodes = range(root, 0, -1)
	mid = len(nodes) // 2
	lst = [(nodes[0], nodes[1:mid+1])]
	lst.append((nodes[0], nodes[mid+1:]))
	while lst:
		parent, nodes = lst.pop(0)
		if nodes[0] in q:
			p[q.index(nodes[0])] = parent
		mid = len(nodes) // 2
		if len(nodes[:mid]) >= 1:
			lst = [(nodes[0], nodes[1:mid+1])] + lst
			lst = [(nodes[0], nodes[mid+1:])] + lst
	return p