from map import Map
from state import State
import tkinter as tk
from glob import Victory, Death
from screens import TextState, PauseState

class   Game(State):
    def __init__(self, parent, machine, level = 1):
        super().__init__(parent, machine)
        self.changeLevel(level)
        self.done = False
        self.map.bind("<Escape>", lambda e: self.machine.push_later(PauseState(self.parent, self.machine)))

    def changeLevel(self, level):
        self.level = level
        filename = "Levels/niveau" + str(level) + ".txt"
        try:
            self.map.load(filename)
        except AttributeError:
            self.map = Map(self, filename)
            self.map.pack(fill=tk.BOTH, expand=tk.YES)
        except FileNotFoundError:
            self.machine.push_later(TextState(self.parent, self.machine, "Youuuuuuuuu WIN: No more level!"))
            self.pop()
            self.done = True

    def update(self, dt):
        try:
            self.map.update(dt)
        except Victory:
            self.changeLevel(self.level + 1)
            if not self.done:
                self.machine.push_later(TextState(self.parent, self.machine, "Youuuuuuu WIN! Next level: " + str(self.level)))
        except Death:
            self.machine.push_later(TextState(self.parent, self.machine, "You're dead bitch!"))
            self.pop()

    def focus(self):
        self.map.focus_set()
    
    def show(self):
        self.map.show()
