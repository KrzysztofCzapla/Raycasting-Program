import pygame, math
from SETTINGS import *


class Raytracer():
	def __init__(self, game):
		self.game = game
		self.raysNumber = RAYS_NUMBER

		self.player = self.game.player
		self.playerX = PLAYER_X
		self.playerY = PLAYER_Y




	
	
	def update(self):
		# rayangle is player angle minus FOV/2, so first ray is the first from left
		# adding small number so theres no dividing by zero
		rayangle = self.player.playerAngle - FOV/2 + 0.0001

		# getting tile pos, its without fractions
		player_tile_pos = (int(self.player.playerX),int(self.player.playerY))

		# calculating every ray
		for ray in range(self.raysNumber):



			offset = 0.0001

			
			# VERTICAL LINES

			# depending on if were looking from left or right we need to check the right tile
			# dx is the distance between the tiles which is 1 or -1 depending on the side were looking
			if math.cos(rayangle) > 0:
				Ver_X = player_tile_pos[0] + 1
				dx = 1


			else:
				Ver_X = player_tile_pos[0] - 0.00001
				dx = -1 


			# Distance to the first vertical line crossing point
			VerticalInitialDistance = (Ver_X - self.player.playerX)/math.cos(rayangle)

			# Dsitance between crossing points in every tile ray is going thru
			VerticalTileDistance = dx/math.cos(rayangle)

			# Number of how many vertical crossings except the initial one
			VerDistanceHowMany = 0

			# Y of first crossing, simple trigonometry
			Ver_Y = math.sin(rayangle)*VerticalInitialDistance + self.player.playerY

			 


			# Checking if it hit the tiles
			while (int(Ver_X),int(Ver_Y)) not in self.game.map.map and VerDistanceHowMany<20:
					# ver_x is always plus one
					Ver_X += dx
					VerDistanceHowMany +=1
					# calculating Y distance between 2 crossings
					Ver_Y += math.sin(rayangle)*VerticalTileDistance

			# adding up distances after hitting wall
			VerticalFinalDistance = VerticalInitialDistance + VerticalTileDistance*VerDistanceHowMany

			
			

			# HORIZONTAL

			# Same logic as above but with horizontal lines, trigonometry is kinda different tho

			if math.sin(rayangle) > 0:
				Hor_Y = player_tile_pos[1] +1
				dy = 1
			else:
				Hor_Y = player_tile_pos[1] - 0.00001
				dy = -1 

			HorizontalInitialDistance = (Hor_Y - self.player.playerY)/math.sin(rayangle)
			HorizontalTileDistance = dy/math.sin(rayangle)
			HorDistanceHowMany = 0
			Hor_X = math.cos(rayangle)*HorizontalInitialDistance + self.player.playerX

			while (int(Hor_X),int(Hor_Y)) not in self.game.map.map and HorDistanceHowMany<20:
					Hor_Y += dy
					HorDistanceHowMany +=1
					Hor_X += math.cos(rayangle)*HorizontalTileDistance


			HorizontalFinalDistance = HorizontalInitialDistance + HorizontalTileDistance*HorDistanceHowMany
			

				

			# The closest one is the one that doesnt go thru wall
			if HorizontalFinalDistance < VerticalFinalDistance:
				TextureType = self.game.map.map[(int(Hor_X),int(Hor_Y))]-1
				FinalDistance = HorizontalFinalDistance
				if math.sin(rayangle) > 0:
					offset = Hor_X % 1

				else:

					offset = 1 - (Hor_X % 1)

			else:
				TextureType = self.game.map.map[(int(Ver_X),int(Ver_Y))]-1
				FinalDistance = VerticalFinalDistance
				if math.cos(rayangle) > 0:
					offset = Ver_Y % 1

				else:

					offset = 1 - (Ver_Y % 1)

			# deleting fisheye effect
			FinalDistance *= math.cos(self.player.playerAngle - rayangle)


			# trigonometry for calculating screenlenght according to width and pov
			ScreenLength = WIDTH/2/math.tan(FOV/2)

			# calculating the wall height based on actual screen size and finaldistance, which is in small numbers
			WallHeight = ScreenLength/FinalDistance
			
			if WallHeight > HEIGHT*15:
				WallHeight = HEIGHT*15

			# color based on distance
			color = 255/ (1 + FinalDistance ** 5 * 0.00002)

			# the actual drawing
			#pygame.draw.rect(self.game.screen,(color,color,color),((ray-1)*SCALE,HEIGHT/2-WallHeight/2,SCALE,WallHeight))
			#print(TextureType)

			texturePart = self.game.imagehandler.textures[TextureType].subsurface(((TEXTURE_SIZE-SCALE)*offset,0,SCALE,TEXTURE_SIZE))

			texturePart = pygame.transform.scale(texturePart,(int(SCALE),int(WallHeight)))

			self.game.screen.blit(texturePart, ((ray-1)*SCALE,HEIGHT/2-WallHeight/2))
	
			#pygame.draw.circle(self.game.screen,(0,100,0),(0,1),20)
			# adding DELTA to move on to another ray
			rayangle += RAY_DELTA_ANGLE
			
				


	def draw(self):
		pass
		#pygame.draw.line(self.game.screen,(200,50,0),(self.playerX*TILE_SIZE_2D,self.playerY*TILE_SIZE_2D),(self.playerX*TILE_SIZE_2D+x,self.playerY*TILE_SIZE_2D+y))

