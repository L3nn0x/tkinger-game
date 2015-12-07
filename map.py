from glob import *
from tkinter import *
from entity import *
from enemies import *
from perso import *

class Map(Canvas):
    def __init__(self, parent, filename, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.perso = None
        self.load(filename)

    def load(self, filename):
        self.delete("all")
        self.entities = []
        with open(filename, "r") as f:
            lines = [l.rstrip("\r\n") for l in f]
            self.maxRed = int(lines[0])
            self.maxGreen = int(lines[1])
            self.w = int(lines[2])
            self.h = int(lines[3])
            self.map = "".join(lines[4:])
            for i in range(len(self.map)):
                if self.map[i] == '0':
                    self.entities.append(Wall(self, (i % self.w, i // self.w), 0))
                elif self.map[i] == "s":
                    self.entities.append(Exit(self, (i % self.w, i // self.w)))
                elif self.map[i] == "j":
                    if self.perso == None:
                        self.perso = Perso(self, (i % self.w, i // self.w))
                    else:
                        self.perso.pos = (i % self.w, i // self.w)
                        self.perso.reset()
        for i in range(self.w):
            self.entities.append(Wall(self, (i, -1), 0))
            self.entities.append(Wall(self, (i, self.h), 0))
        for i in range(self.h):
            self.entities.append(Wall(self, (-1, i), 0))
            self.entities.append(Wall(self, (self.w, i), 0))

    def show(self):
        for i in self.entities:
            i.show()
        self.perso.show()

    def update(self, dt):
        for i in self.entities:
            i.update(dt, self)
        self.perso.update(dt, self)

    def entity_type(self, coord):
        for i in self.entities:
            if i.pos == coord:
                if isinstance(i, Wall): 
                    return WALL
                elif isinstance(i, Red): 
                    return REDENNEMY
                elif isinstance(i, Green): 
                    return GREENENNEMY
                elif isinstance(i, Exit): 
                    return FINISH
                elif isinstance(i, Perso):
                    return PERSO
        return NOTHING

