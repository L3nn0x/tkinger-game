from glob import *
from entity import *

class Wall(Entity):
    """docstring for Wall"""
    def __init__(self,screen,pos,nb):
        filename = "Images/wall.gif"
        super().__init__(screen,filename,pos)

class Red(Entity):
    """docstring for Red"""
    def __init__(self,screen,pos):
        filename = "Images/red.gif"
        super().__init__(screen,filename,pos)

    def update(self,dt,level):
        import random
        directions = [NORTH, SOUTH, WEST, EAST]
        typ = super().move(directions[random.randInt(0, 3)], level)
        while typ == WALL:
            if typ == PERSO:
                raise ValueError
                typ = super().move(directions[random.randInt(0, 3)], level)
			
class Green(Entity):
    """docstring for green"""
    def __init__(self,screen,pos):
        filename = "Images/green.gif"
        super().__init__(screen,filename,pos)

class Exit(Entity):
    """docstring for Exit"""
    def __init__(self,screen,pos):
        filename = "Images/Exit.gif"
        super().__init__(screen,filename,pos)
