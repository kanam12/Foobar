dist = {}
ways = {}

def answer(src, dest):
    if src < 8:
        src = (0, src)
    else:
        src = src%8, src//8
    if dest < 8:
        dest = (0, dest)
    else:
        dest = dest%8, dest//8

    queue = [src]
    dist[src] = 0
    ways[src] = 1

    while len(queue):
        curr = queue[0]
        queue.pop(0)
        if curr == dest:
            return dist[curr]
        #if src[1] == dest[1] and src[0]+1 == dest[0] or src[0]-1 == dest[0]:
            #return 3

        for move in [ (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1) ]:
            next_pos = curr[0]+move[0], curr[1]+move[1]
            if next_pos[0] > dest[0] or next_pos[1] > dest[1] or next_pos[0] < 1 or next_pos[1] < 1:
                continue
            if next_pos not in dist:
                dist[next_pos] = dist[curr]+1
                ways[next_pos] = ways[curr]
                queue.append(next_pos)
            if next_pos in dist and dist[next_pos] == dist[curr]+1:
                ways[next_pos] += ways[curr]






