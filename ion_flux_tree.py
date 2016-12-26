def tree(h, q):
    if h == 1:
        return [-1]
    root = (2**h) - 1
    for i in range(len(q)):
        leaf = 1
        nodes = [(-1, root, leaf)]
        while nodes:
            parent, curr, leaf = nodes.pop(0)
            mid = (curr+leaf)//2
            if curr == q[i]:
                q[i] = parent
                break
            elif q[i] >= mid and q[i] < curr:
                if curr - 1 > 0:
                    nodes = [(curr, curr - 1, mid)]
            else:
                if curr - mid > 0:
                    nodes = [(curr, mid - 1, leaf)]
    return q