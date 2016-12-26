def tree(h, q):
	if h == 1:
        return [-1]
    root = (2**h) - 1
    for i in range(len(q)):
        end = 1
        nodes = [(-1, root, end)]
        while nodes:
            parent, curr, end = nodes.pop(0)
            mid = (curr+end)//2
            if curr == q[i]:
                q[i] = parent
                break
            elif q[i] >= mid and q[i] < curr:
                if curr - 1 > 0:
                    nodes = [(curr, curr - 1, mid)]
            else:
                if range(mid, curr):
                    nodes = [(curr, mid - 1, end)]
    return q