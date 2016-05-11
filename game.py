from create import *
from person import *
from ghost import *

grid = create_grid()
print_grid(grid)

g1 = Ghost(grid, 3, 4)
g2 = Ghost(grid, 17, 4)
#print_grid(grid)

score = 0
while 1:
	print_grid(grid)

	print "Score: ", 
	print score

	print "Move: ",
	move = raw_input()
	print move

	if move == 'q':
		print "Exit..!!"
		break