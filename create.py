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

	grid.append("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
	grid.append("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
	grid.append("xx...................................................xx")
	grid.append("xx...xx.........................................xx...xx")
	grid.append("xx....xx.......................................xx....xx")
	grid.append("xx.....xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.....xx")
	grid.append("xx...................................................xx")
	grid.append("xx...................................................xx")
	grid.append("xx...................................................xx")
	grid.append("xx........xxxxxxx.......xxxxxxx.......xxxxxxx........xx")
	grid.append("xx........x.....x.......x.....x.......x..............xx")
	grid.append("xx........x.....x.......x.....x.......x..............xx")
	grid.append("xx........x..xxxx.......x.xxx.x.......x..............xx")
	grid.append("xx........x.............x.....x.......x..............xx")
	grid.append("xx........x.............x.....x.......x..............xx")
	grid.append("xx........x.............x.....x.......xxxxxxx........xx")
	grid.append("xx...................................................xx")
	grid.append("xx...................................................xx")
	grid.append("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
	grid.append("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

	return grid

def print_grid(grid):
	print
	print
	for i in grid:
		print i
	print
	print
