import pygame, math
from SETTINGS import *


class Player():
	def __init__(self, game):
		self.game = game
		self.playerAngle = 0
		self.playerSpeed = PLAYER_SPEED
		self.playerX = PLAYER_X
		self.playerY = PLAYER_Y
		self.playerPos = (self.playerX,self.playerY)
		self.MousePosX = WIDTH/2
		self.MousePosXOld = WIDTH/2

	# checks if x and y arent in any walls
	def checkCollisions(self,x,y):
		return (x,y)  in self.game.map.map
			
	def mouse(self):
		# mouse realtive pos
		self.rel = pygame.mouse.get_rel()[0]


		self.rel = max(-MOUSE_MAX_MOVE, min(MOUSE_MAX_MOVE,self.rel))

		# making sure mouse stays in the window
		if pygame.mouse.get_pos()[0] < MOUSE_MAX_LEFT or pygame.mouse.get_pos()[0] > MOUSE_MAX_RIGHT:
			pygame.mouse.set_pos([WIDTH/2,HEIGHT/2])
			print("MOUSE CORRECTION")
		

		
		self.playerAngle += PLAYER_ANGLE_SPEED*self.game.delta*self.rel

		# Calculating sky background movement
		self.game.imagehandler.skyblockX -= PLAYER_ANGLE_SPEED*self.game.delta*self.rel*800			

	def movement(self):


		# x,y for moving, resets everytime
		x,y  = 0, 0


		# here checking for keys
		# This is basically trigonometry cos(angle) = speed/x, from this we can calculate x and y

		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			x  += self.playerSpeed*math.cos(self.playerAngle)
			y  += self.playerSpeed*math.sin(self.playerAngle)
		if keys[pygame.K_s]:
			x  += -self.playerSpeed*math.cos(self.playerAngle)
			y  += -self.playerSpeed*math.sin(self.playerAngle)
		if keys[pygame.K_a]:
			y  += -self.playerSpeed*math.cos(self.playerAngle)
			x  += self.playerSpeed*math.sin(self.playerAngle)
		if keys[pygame.K_d]:
			y  += self.playerSpeed*math.cos(self.playerAngle)
			x  += -self.playerSpeed*math.sin(self.playerAngle)

		# Normalizing angles
		if self.playerAngle > 6.28 and self.playerAngle < 6.3:
			self.playerAngle = 0
		if self.playerAngle < -6.28 and self.playerAngle > -6.3:
			self.playerAngle = 0

		# giving x and y in int, because walls are in ints too(not floats) and we are comapring them in checkCollisions
		if not self.checkCollisions(int(self.playerX+ x*self.game.delta),int(self.playerY)):
			self.playerX += x*self.game.delta
		if not self.checkCollisions(int(self.playerX),int(self.playerY+ y*self.game.delta)):
			self.playerY += y*self.game.delta
	

		
	def update(self):
		self.movement()
		self.mouse()


	def draw(self):
		#pass
		pygame.draw.circle(self.game.screen,(0,100,0),(self.playerX*TILE_SIZE_2D,self.playerY*TILE_SIZE_2D),10)
		x = 50*math.cos(self.playerAngle)
		y = 50*math.sin(self.playerAngle)
		pygame.draw.line(self.game.screen,(200,50,0),(self.playerX*TILE_SIZE_2D,self.playerY*TILE_SIZE_2D),(self.playerX*TILE_SIZE_2D+x,self.playerY*TILE_SIZE_2D+y))

		

