from create import *
from person import *
from ghost import *
from pacman import *

grid = create_grid()
print_grid(grid)

g1 = Ghost(grid, 3, 4)
g2 = Ghost(grid, 17, 4)
#print_grid(grid)

p = Pacman(grid, 4, 20)

score = 0
while 1:
	print_grid(grid)

	print "Score: ", 
	print score

	print "Move: ",
	mov = raw_input()
	print mov

	if mov == 'q':
		print "Exit..!!"
		break

	elif mov=='w' or mov=='s' or mov=='a' or mov=='d' : 
		p.move(grid, mov)

	else:
		print "Please enter correct keys..!!!"

	