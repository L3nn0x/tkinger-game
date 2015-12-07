from glob import *
import tkinter as tk

class   Entity:
    def __init__(self, screen, filename, pos):
        self.img = screen.create_image(pos, tk.PhotoImage(file=filename))
        self.screen = screen
        self.pos = pos
        self.dead = False

    def show(self):
        self.screen.coord(self.img, self.pos)

    def move(self, pos, level):
        old = self.pos
        self.pos = tuple((x + y for x, y in zip(self.pos, pos)))
        typ = level.type(self.pos)
        if typ == WALL or typ == GREENENNEMY:
            self.pos = pos
        elif typ == REDENNEMY:
            self.dead = True
        return typ

    def update(self, dt):
        pass
