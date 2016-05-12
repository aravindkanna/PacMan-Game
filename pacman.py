from person import *

class Pacman(Person):

	def __init__(self, grid, x, y):
		self.x = x
		self.y = y
		grid[x][y] = 'P'

	def set_pos(self, grid):
		grid[self.x][self.y] = 'P'
