from person import *

class Ghost(Person):

	def __init__(self, grid, x, y):
		self.x = x
		self.y = y
		grid[x][y] = 'G'

	"""def is_move(self, grid, x, y):
		if grid[x][y] == 'x':
			return false
		return true
		"""

	def set_pos(self, grid):
		grid[self.x][self.y] = 'G'