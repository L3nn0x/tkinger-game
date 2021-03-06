from glob import *
import tkinter as tk

class   Entity:
    """Base class for everything on the screen"""
    def __init__(self, screen, filename, pos):
        self.photo = tk.PhotoImage(file=filename)
        self.img = screen.create_image(*tuple(map(lambda x: x*SIZE+CST, pos)), image=self.photo)
        self.screen = screen
        self.pos = pos

    """reset the Entity (if you want to recreate the image without openning the file again)"""
    def reset(self):
        self.img = self.screen.create_image(*tuple(map(lambda x: x*SIZE+CST, self.pos)), image=self.photo)

    """actually move the printed object on screen"""
    def show(self):
        self.screen.coords(self.img, *tuple(map(lambda x: x*SIZE+CST, self.pos)))

    """moves the entity and checks for collisions"""
    def move(self, pos, level):
        old = self.pos
        self.pos = tuple((x1 + x2 for x1, x2 in zip(self.pos, pos)))
        typ = level.entity_type(self.pos)
        if typ == WALL or typ == GREENENNEMY:
            self.pos = old
        return typ

    def update(self, dt, level):
        pass

