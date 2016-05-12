

class Person(object):
	def __init__(self, grid, x, y):
		self.x = x
		self.y = y
		self.grid = grid
		self.score = 0

	def set_pos(self, grid):
		grid[self.x][self.y] = 'p'

	def is_move(self, grid, x, y):
		if grid[x][y]=='x':
			return False
		return True

	def is_coin(self, grid, x, y):
		if grid[x][y] == 'C':
			return True
		return False

	def move(self, grid, move):
		if move == 'a':
			if self.is_move(grid, self.x, self.y-1):
				if self.is_coin(grid, self.x, self.y-1):
					self.score = self.score + 1
				grid[self.x][self.y] = '.'
				self.y = self.y-1
				self.set_pos(grid)
		elif move == 'd':
			if self.is_move(grid, self.x, self.y+1):
				if self.is_coin(grid, self.x, self.y+1):
					self.score = self.score + 1
				grid[self.x][self.y] = '.'
				self.y = self.y+1
				self.set_pos(grid)
		elif move == 'w':
			if self.is_move(grid, self.x-1, self.y):
				if self.is_coin(grid, self.x-1, self.y):
					self.score = self.score + 1
				grid[self.x][self.y] = '.'
				self.x = self.x-1
				self.set_pos(grid)
		elif move == 's':
			if self.is_move(grid, self.x+1, self.y):
				if self.is_coin(grid, self.x+1, self.y):
					self.score = self.score + 1
				grid[self.x][self.y] = '.'
				self.x = self.x+1
				self.set_pos(grid)

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def get_point(self):
		return (self.x, self.y)

	def get_score(self):
		return self.score