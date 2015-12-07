from glob import *
from tkinter import *
from entity import *

class Map(Canvas):
  def __init__(self, parent, filename, *args, **kwargs):
    super.__init__(parent, *args, **kwargs)
    self.filename = filename
    self.entities = []
    with open(filename, "r") as f:
      lines = [l.rstrip("\r\n") for l in f]
      self.maxRed = int(lines[0])
      self.maxGreen = int(lines[1])
      self.w = int(lines[2])
      self.h = int(lines[3])
      self.map = "".join(lines[4:])
    for i in range(len(self.map)):
      if self.map[i] == 0:
        pass
      elif self.map[i] == 1:
        self.entities.append(Wall(self, (i % self.w, i // self.w), 0))
      elif self.map[i] == "s":
        self.entities.append(Exit(self, (i % self.w, i // self.w)))
      elif self.map[i] == "j":
        self.entities.append(Perso(self, (i % self.w, i // self.w)))
      else:
        raise NameError('Invalid character in map file')

    def show(self):
      for i in self.entities:
        i.show()

    def update(self, dt):
      for i in self.entities:
        i.update(dt, self)

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
        
