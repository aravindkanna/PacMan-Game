"""
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	xx...................................................xx
	xx...xx.........................................xx...xx
	xx....xx.......................................xx....xx
	xx.....xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.....xx
	xx...................................................xx
	xx...................................................xx
	xx...................................................xx
	xx........xxxxxxx.......xxxxxxx.......xxxxxxx........xx
	xx........x.....x.......x.....x.......x..............xx
	xx........x.....x.......x.....x.......x..............xx
	xx........x..xxxx.......x.xxx.x.......x..............xx
	xx........x.............x.....x.......x..............xx
	xx........x.............x.....x.......x..............xx
	xx........x.............x.....x.......xxxxxxx........xx
	xx...................................................xx
	xx...................................................xx
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

	20x55 play grid
"""

def create_grid():
	grid = []

	grid.append(list("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"))
	grid.append(list("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"))
	grid.append(list("xx...................................................xx"))
	grid.append(list("xx...xx.........................................xx...xx"))
	grid.append(list("xx....xx.......................................xx....xx"))
	grid.append(list("xx.....xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.....xx"))
	grid.append(list("xx...................................................xx"))
	grid.append(list("xx...................................................xx"))
	grid.append(list("xx...................................................xx"))
	grid.append(list("xx........xxxxxxx.......xxxxxxx.......xxxxxxx........xx"))
	grid.append(list("xx........x.....x.......x.....x.......x..............xx"))
	grid.append(list("xx........x.....x.......x.....x.......x..............xx"))
	grid.append(list("xx........x..xxxx.......x.xxx.x.......x..............xx"))
	grid.append(list("xx........x.............x.....x.......x..............xx"))
	grid.append(list("xx........x.............x.....x.......x..............xx"))
	grid.append(list("xx........x.............x.....x.......xxxxxxx........xx"))
	grid.append(list("xx...................................................xx"))
	grid.append(list("xx...................................................xx"))
	grid.append(list("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"))
	grid.append(list("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"))

	return grid

def print_list(l):
	for i in l:
		print i,
	print

def print_grid(grid):
	print
	print
	for i in grid:
		print_list(i)
	print
	print
