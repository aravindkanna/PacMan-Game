from create import *
from person import *
from ghost import *
from pacman import *
from random import randint

grid = create_grid()
#print_grid(grid)

g1 = Ghost(grid, 3, 4)
g2 = Ghost(grid, 17, 4)
g3 = Ghost(grid, 8, 50)
g4 = Ghost(grid, 16, 48)
#print_grid(grid)

p = Pacman(grid, 4, 20)

score = 0
while 1:
	print_grid(grid)

	print "Score: ", 
	print score

	print "Move: ",
	mov = raw_input()
	#print mov

	if mov == 'q':
		print "Exit..!!"
		print "Your Score: ",
		print score
		break

	elif mov=='w' or mov=='s' or mov=='a' or mov=='d' : 
		p.move(grid, mov)

	else:
		print "Please enter correct keys..!!!"

	rand1 = randint(0, 9)%4
	rand2 = randint(0, 9)%4
	rand3 = randint(0, 9)%4
	rand4 = randint(0, 9)%4

	if rand1 == 0:
		g1.move(grid, 'w')
	elif rand1 == 1:
		g1.move(grid, 's')
	elif rand1 == 2:
		g1.move(grid, 'a')
	elif rand1 == 3:
		g1.move(grid, 'd')

	if rand2 == 0:
		g2.move(grid, 'w')
	elif rand2 == 1:
		g2.move(grid, 's')
	elif rand2 == 2:
		g2.move(grid, 'a')
	elif rand2 == 3:
		g2.move(grid, 'd')

	if rand3 == 0:
		g3.move(grid, 'w')
	elif rand3 == 1:
		g3.move(grid, 's')
	elif rand3 == 2:
		g3.move(grid, 'a')
	elif rand3 == 3:
		g3.move(grid, 'd')

	if rand4 == 0:
		g4.move(grid, 'w')
	elif rand4 == 1:
		g4.move(grid, 's')
	elif rand4 == 2:
		g4.move(grid, 'a')
	elif rand4 == 3:
		g4.move(grid, 'd')

	pnts = (g1.get_point(), g2.get_point(), g3.get_point(), g4.get_point())
	end = False
	for i in pnts:
		if i == p.get_point():
			end = True

	score = p.get_score()

	if end:
		print "*******GAME*********OVER*******"
		print "Your Score: ",
		print score
		break;
