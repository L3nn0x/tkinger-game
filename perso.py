from glob import *
from entity import Entity

class   Perso(Entity):
    """Player class"""
    def __init__(self, screen, pos):
        super().__init__(screen, "Images/perso.gif", pos)
        self.speed = (0, 0)
        self.time = 0
        self.win = False
        screen.bind("<Left>", lambda e: self.handleEvent(WEST))
        screen.bind("<Right>", lambda e: self.handleEvent(EAST))
        screen.bind("<Up>", lambda e: self.handleEvent(NORTH))
        screen.bind("<Down>", lambda e: self.handleEvent(SOUTH))
        screen.bind("<KeyRelease>", lambda e: self.handleEvent((0, 0)))

    """Reset the player for the next level"""
    def reset(self, pos):
        self.pos = pos
        self.speed = (0, 0)
        self.time = 0
        self.win = False
        super().reset()

    """check events"""
    def handleEvent(self, speed):
        self.speed = speed

    """update the player position and status"""
    def update(self, dt, level):
        self.time += dt
        if self.time >= 150:
            if self.win:
                raise Victory
            self.time = 0
            typ = super().move(self.speed, level)
            if typ == FINISH:
                self.win = True
            elif typ == REDENNEMY:
                raise Dead
