import pygame
from SETTINGS import *


class Enemy():
	def __init__(self,game,x,y,image):
		self.game = game
		self.x = x
		self.y = y
		self.image = image
		self.angle = 0
		self.ray = 0



	def update(self):
		pass

	def draw(self):
		pass


class EnemyHandler():
	def __init__(self,game):
		self.game = game
		self.enemyImage = pygame.image.load("enemy.png").convert_alpha()

		self.enemies = []

		self.enemies.append(Enemy(self.game, 1,1,self.enemyImage))


	def update(self):
		for enemy in self.enemies:
			dy = enemy.y-self.game.player.playerY
			dx = enemy.x-self.game.player.playerX+0.0001
			enemy.angle = math.tan((dy)/(dx))
			
			enemy.angle =  enemy.angle - self.game.player.playerAngle

			#if (dy > 0 and self.game.player.playerAngle > math.pi) or (dx<0 and dy>0):
				#enemy.angle += math.tau


			enemy.ray = enemy.angle/RAY_DELTA_ANGLE

			


	def draw(self):
		for enemy in self.enemies:
			pygame.draw.circle(self.game.screen,(0,200,0),(200,200),10)
			self.game.enemyhandler.enemyImage = pygame.transform.scale(self.game.enemyhandler.enemyImage,(self.game.enemyhandler.enemyImage.get_width(),int(200)))

			#self.game.screen.blit(self.game.enemyhandler.enemyImage, ((enemy.ray-1)*SCALE,HEIGHT/2-self.game.enemyhandler.enemyImage.get_height()/2))

