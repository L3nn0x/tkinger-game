from glob import *

class Wall(Entity):
	"""docstring for Wall"""
	def __init__(self,screen,pos,nb):
		filename = "wall.bnp"
		super().__init__(screen,filename,pos)

class Red(self):
	"""docstring for Red"""
	def __init__(self,screen,pos):
		filename = "red.bnp"
		super().__init__(screen,filename,pos)

	def update(self,dt,level):
		import random
		directions = [NORTH, SOUTH, WEST, EAST]
		typ = super().move(directions[random.randInt(0, 3)], level)
		while typ == WALL:
			if typ == PERSO:
				raise ValueError
			typ = super().move(directions[random.randInt(0, 3)], level)
			
class Green(self):
	"""docstring for green"""
	def __init__(self,screen,pos):
		filename = "green.bnp"
		super().__init__(screen,filename,pos)

class Exit(self):
	"""docstring for Exit"""
	def __init__(self,screen,pos):
		filename = "exit.bnp"
		super().__init__(screen,filename,pos)
