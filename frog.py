# Frog class to create a Frog object.

# MODULES
import pygame



# LOG CLASS
class Frog:


	# INITIALIZE
	def __init__(self, window, color, x, y, radius, vel):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.radius = radius
		self.vel = vel


	# DRAW FROG
	def draw(self):
		pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)

	# MOVE FROG: From left to right, based off which log it's on.
	def move(self):
		# Move log
		self.x += self.vel


		# Should NOT need these, as frog is dependent on log and log already has the dependencies on hitting walls.
		# # If log hits wall...
		# if self.x <= 0 or self.x >= 300:

		# 	# Shift direction.
		# 	self.vel *= -1
