dist = {}

def answer(src, dest):
	src = (src%8, src//8)
	dest = dest%8, dest//8
	queue = [src]
	for x in range(8):
		for y in range(8):
			dist[(x, y)] = -1
	dist[src] = 0
	while queue:
		curr = queue.pop(0)
		for move in [ (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1) ]:
			next_pos = curr[0]+move[0], curr[1]+move[1]
			if next_pos[0] < 8 and next_pos[1] < 8 and next_pos[0] >= 0 and next_pos[1] >= 0:
				newDist = dist[curr] + 1
				if dist[next_pos] == -1:
					dist[next_pos] = newDist
					queue.append(next_pos)

	return dist[dest]