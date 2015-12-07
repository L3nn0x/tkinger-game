from glob import *
from entity import Entity

class   Perso(Entity):
    def __init__(self, screen, pos):
        super().__init__(screen, "perso.gif", pos)
        self.speed = (0, 0)
        self.time = 0
        screen.bind("<Left>", lambda e: self.handleEvent(WEST))
        screen.bind("<Right>", lambda e: self.handleEvent(EAST))
        screen.bind("<Up>", lambda e: self.handleEvent(NORTH))
        screen.bind("<Down>", lambda e: self.handleEvent(SOUTH))

    def handleEvent(self, speed):
        self.speed = speed

    def update(self, dt, level):
        self.time += dt
        if self.time >= 250:
            self.time = 0
            typ = super().move(self.speed, level)
            if typ == FINISH:
                raise KeyError
            elif typ == REDENNEMY:
                raise ValueError
