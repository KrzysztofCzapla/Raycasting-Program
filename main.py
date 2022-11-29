import pygame, math
from SETTINGS import *
from map import *
from player import *
from raycasting import *
from imagehandler import *
from enemyhandler import *

class Game():
	def __init__(self):
		# if game is supposed to run
		self.isRunning = True 
		# loading pygame
		pygame.init()
		# setting up screen
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		# setting clock for FPS and DeltaTime
		self.clock = pygame.time.Clock()
		# setting DeltaTime(It is needed for smooth movement)
		#
		#	Sometimes Program runs faster, sometimes slower;
		#	With DeltaTime we can stabilize movement speed
		#
		self.delta = 1

		self.map = Map(self)
		self.player = Player(self)
		self.raytracer = Raytracer(self)
		self.imagehandler = ImageHandler(self)
		self.enemyhandler = EnemyHandler(self)

		pygame.mouse.set_visible(False)

	def checkEvents(self):
		# Checking every event for clicking X in top right corner
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					self.isRunning = False

	def update(self):
		# updating clock
		self.clock.tick(FPS)
		# updating delta
		self.delta = self.clock.tick(FPS)/10
		
		# fps meter
		pygame.display.set_caption(str(int(self.clock.get_fps())))

		self.map.update()
		self.player.update()
		self.imagehandler.update()
		self.enemyhandler.update()
		
	def draw(self):
		self.screen.fill((75,70,70))
		# updating screen with everyting we draw
		self.imagehandler.draw()
		
		self.raytracer.draw()
		
		self.raytracer.update()
		#self.enemyhandler.draw()
		#self.map.draw()
		#self.player.draw()
		pygame.display.update()


	def run(self):
		self.checkEvents()
		self.update()
		self.draw()
		

if __name__ == "__main__":
	game = Game()
	while game.isRunning:
		game.run()