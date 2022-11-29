import pygame, math
from SETTINGS import *
O = False

miniMap = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	       [1,O,O,3,O,O,O,O,O,O,O,1,O,O,O,2,O,O,O,1,O,O,O,1],
		   [1,O,O,3,O,O,O,2,2,O,O,1,O,O,O,2,2,2,O,1,O,O,O,1],
		   [1,O,O,3,O,O,O,2,2,O,O,O,O,O,O,O,O,O,O,1,O,O,O,1],
		   [1,O,O,O,O,O,O,O,O,O,O,1,O,O,O,O,O,O,O,1,O,O,O,1],
		   [1,O,O,O,O,O,O,O,O,O,O,1,O,O,O,O,O,O,O,O,O,O,O,1],
		   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]	
		]

class Map():
	def __init__(self, game):
		self.game = game
		self.miniMap = miniMap
		self.map = {}
		# --setting self.map with type of block--
		# y - number of row, j - content of row
		for y, j in enumerate(self.miniMap):
			# x - number of column, j - content of element
			for x, i in enumerate(j):
				# if it is a wall, not a space
				if i:
					# taking position of column and row and putting in content so we know...
					# ... where are walls and what type
					self.map[(x,y)] = i
		

	def update(self):
		pass

	def draw(self):
		#pass
		
		for j in self.map:

			pygame.draw.rect(self.game.screen,(255,255,255),(j[0]*TILE_SIZE_2D,j[1]*TILE_SIZE_2D,TILE_SIZE_2D,TILE_SIZE_2D),1)

