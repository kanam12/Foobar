def possible_paths(start):
	board = [[x for x in range(8)] for y in range(8)]
	if start < 8:
		src = (0, start)
	else:
		src = start%8, start//8
	solns = []
	count = 1
	board[src[0]][src[1]] = 0
	#for move in [ (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1) ]:
		#next_pos = curr[0]+move[0], curr[1]+move[1]

	
	functions = [lambda x: x+6, lambda x: x+10, lambda x: x+15, lambda x: x+17, lambda x: x-6, lambda x: x-10, lambda x: x-15, lambda x: x-17]
	for fn in functions:
		if fn(start) in range(64):
			solns.append(fn(start))
			if fn(start) < 8:
				new = (0, fn(start))
			else:
				new = (fn(start))%8, (fn(start))//8
			board[new[0]][new[1]] = count
	for item in solns[1:]:
		possible_paths(item)
	print(board)
	return solns




