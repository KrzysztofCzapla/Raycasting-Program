import pygame
from SETTINGS import *

class ImageHandler():
	def __init__(self,game):
		self.textures = []
		self.texturesNum = 3
		self.game = game

		for texture in range(self.texturesNum):
			self.textures.append(pygame.image.load("%s.png" % (texture+1)).convert_alpha())

		self.sky = pygame.image.load("night-sky-stars.jpeg").convert_alpha()

		self.skyblockX = 0


	def update(self):
		
		
		if self.skyblockX >= 1920 or self.skyblockX <= -1920:
			self.skyblockX = 0

	def draw(self):
		
		# drawing sky, 3 times so theres no gaps
		self.game.screen.blit(self.game.imagehandler.sky, (self.skyblockX,-(self.game.imagehandler.sky.get_height()-HEIGHT/2)))
		self.game.screen.blit(self.game.imagehandler.sky, (self.skyblockX-self.game.imagehandler.sky.get_width(),-(self.game.imagehandler.sky.get_height()-HEIGHT/2)))
		self.game.screen.blit(self.game.imagehandler.sky, (self.skyblockX+self.game.imagehandler.sky.get_width(),-(self.game.imagehandler.sky.get_height()-HEIGHT/2)))
