# MODULES
import pygame
import random 			# For direction of logs
from frog import Frog
from log import Log
from apple import Apple
from ground import Ground



# INITIALIZE
pygame.init() 											# Initialize 'pygame'.
WIN_X, WIN_Y = 400, 480 								# Set window (x, y).
window = pygame.display.set_mode((WIN_X, WIN_Y)) 		# Create window.
pygame.display.set_caption("Frogger") 					# Title of window.
font = pygame.font.Font('freesansbold.ttf', 32) 		# Properties of Font.
clock = pygame.time.Clock()
run = True 			# Main loop
FPS = 60 			# Speed of game.



# COLORS
WHITE   = (255, 255, 255)
BLACK   = (  0,   0,   0)
L_GRAY  = ( 85,  85,  85)
D_Gray  = (170, 170, 170)
RED     = (255,   0,   0)
GREEN_1 = (  0, 222,   0) 	# Frog
GREEN_2 = (  0, 126,   0) 	# Ground
BROWN   = (140,  64,   0)
BLUE    = (  0,  53, 159)



# INITIALIZE OBJECTS

# 10 ROWS: Each with an 'Y' value.
row = [  0,  50, 100, 150, 200,
	   250, 300, 350, 400, 450]

# ROW 0: Top Ground
top = Ground(window, GREEN_2, 0, row[0], 400, 30)
apple = Apple(window, RED, 200, row[0]+15, 5)

# ROW 1-8: Logs
logs = []
for i in range(8):

	log_y = row[1+i] 				# Increase 'y' by 50.
	rx = random.randint(25, 275) 	# Random placement on row.

	# Direction
	if i % 2 == 0:
		r_vel = random.randint(1, 3)

	else:
		r_vel = random.randint(-3, -1)

	log = Log(window, BROWN, rx, log_y, 100, 25, r_vel)
	logs.append(log)

# ROW 9: Bottom Ground, starting Frog.
bot = Ground(window, GREEN_2, 0, row[9], 400, 30)
frog = Frog(window, GREEN_1, 200, row[9], 10, 3)




# MAIN LOOP
while run:


	# INITIALIZE
	clock.tick(FPS) 					# Speed of game.
	window.fill(BLUE) 				# BACKGROUND: Blue (Water)
	keys = pygame.key.get_pressed() 	# Frog Movement

	# EACH EVENT
	for event in pygame.event.get():

		# IF QUIT...
		if event.type == pygame.QUIT:
			run = False


	# DRAW OBJECTS
	# Log Objects
	for i in range(len(logs)):
		logs[i].move()
		logs[i].draw()

	# Other Objects
	top.draw()
	apple.draw()
	bot.draw()
	frog.draw()


	# Move Frog
	if keys[pygame.K_UP]: 	# 'Up' has different calculations than down or side-to-side.

		# if frog

		# Q: How to check for the NEXT log?

		# TOP GROUND
		if frog.y == row[1]:
			frog.y -= 50

		# LOG[1] or ROW[2]
		if frog.y == row[2]:
			# If enough space to jump on to the next log...
			if logs[0].x+frog.radius <= frog.x <= logs[0].x-frog.radius+100:
				# Jump to the next log.
				frog.y -= 50

		# LOG[2] or ROW[3]
		if frog.y == row[3]:
			# If enough space to jump on to the next log...
			if logs[1].x+frog.radius <= frog.x <= logs[1].x-frog.radius+100:
				# Jump to the next log.
				frog.y -= 50

		# LOG[3] or ROW[4]
		if frog.y == row[4]:
			# If enough space to jump on to the next log...
			if logs[2].x+frog.radius <= frog.x <= logs[2].x-frog.radius+100:
				# Jump to the next log.
				frog.y -= 50

		# LOG[4] or ROW[5]
		if frog.y == row[5]:
			# If enough space to jump on to the next log...
			if logs[3].x+frog.radius <= frog.x <= logs[3].x-frog.radius+100:
				# Jump to the next log.
				frog.y -= 50

		# LOG[5] or ROW[6]
		if frog.y == row[6]:
			# If enough space to jump on to the next log...
			if logs[4].x+frog.radius <= frog.x <= logs[4].x-frog.radius+100:
				# Jump to the next log.
				frog.y -= 50

		# LOG[6] or ROW[7]
		if frog.y == row[7]:
			# If enough space to jump on to the next log...
			if logs[5].x+frog.radius <= frog.x <= logs[5].x-frog.radius+100:
				# Jump to the next log.
				frog.y -= 50

		# LOG[7] or ROW[8]
		if frog.y == row[8]:
			# If enough space to jump on to the next log...
			if logs[6].x+frog.radius <= frog.x <= logs[6].x-frog.radius+100:
				# Jump to the next log.
				frog.y -= 50

		# BOTTOM GROUND
		if frog.y == row[9]:
			# If log[7] is in front of frog.
			if logs[7].x+frog.radius <= frog.x <= logs[7].x-frog.radius+100:
				frog.y -= 50




		# # LOG[0] or ROW[1]
		# if frog.y == row[8]:
		# 	# If enough space to jump on to the next log...
		# 	if log.x+frog.radius <= frog.x <= log.x-frog.radius+100:
		# 		# Jump to the next log.
		# 		frog.y -= 50


	# If Frog is NOT on solid ground (top or bottom), move WITH the log.
	if frog.y != row[0] and frog.y != row[9]:

		# for loop with, 'row[]' is 'log[i-1]'

		# Which ever row we are on, set Frog's velocity to that of the Log it's on.

		for i in range(len(row)):
			# Which ever row frog is on...
			if frog.y == row[i]:
				# Set Frog's velocity to that Log's velocity.
				frog.vel = logs[i-1].vel 	# One less than that of 'row[]'


		# MOVE Frog
		frog.move()



	# UPDATE
	pygame.display.update()

# END LOOP if run == False



# If Main Loop == False
pygame.quit()
