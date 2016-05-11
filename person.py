

class Person(object):
	def __init__(self, grid, x, y):
		self.x = x
		self.y = y
		self.grid = grid

	def set_pos(self, grid):
		grid[self.x][self.y] = 'p'

	def is_move(self, grid, x, y):
		if grid[x][y] == 'x':
			return False
		return True

	def move(self, grid, move):
		if move == 'a':
			if self.is_move(grid, self.x, self.y-1):
				grid[self.x][self.y] = '.'
				self.y = self.y-1
				self.set_pos(grid)
		elif move == 'd':
			if self.is_move(grid, self.x, self.y+1):
				grid[self.x][self.y] = '.'
				self.y = self.y+1
				self.set_pos(grid)
		elif move == 'w':
			if self.is_move(grid, self.x-1, self.y):
				grid[self.x][self.y] = '.'
				self.x = self.x-1
				self.set_pos(grid)
		elif move == 's':
			if self.is_move(grid, self.x+1, self.y):
				grid[self.x][self.y] = '.'
				self.x = self.x+1
				self.set_pos(grid)

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y