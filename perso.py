from glob import *
from entity import Entity

class   Perso(Entity):
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

    def reset(self):
        self.speed = (0, 0)
        self.time = 0
        self.win = False

    def handleEvent(self, speed):
        self.speed = speed

    def update(self, dt, level):
        self.time += dt
        if self.time >= 250:
            if self.win:
                raise KeyError
            self.time = 0
            typ = super().move(self.speed, level)
            if typ == FINISH:
                self.win = True
            elif typ == REDENNEMY:
                raise ValueError
