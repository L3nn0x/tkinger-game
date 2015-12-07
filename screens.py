import tkinter as tk
from state import State

class   TextState(State):
    """State to just print some text and return to the previous state once 2.5sec have passed or a key has been pressed"""
    def __init__(self, parent, machine, text):
        super().__init__(parent, machine)
        self.initUI(text)
        self.time = 0

    def initUI(self, text):
        self.label = tk.Label(self, text=text)
        self.label.pack()
        self.bind("<Key>", lambda e: self.pop())

    def update(self, dt):
        self.time += dt
        if self.time > 2500:
            self.pop()

class   PauseState(TextState):
    """The pause state with it's logic"""
    def __init__(self, parent, machine):
        text = """The game is paused!
        Press <Escape> to return to the menu.
        
                Press any key to unpause."""
        super().__init__(parent, machine, text)
        self.bind("<Escape>", lambda e: self.quit())

    def update(self, dt):
        pass

    def quit(self):
        from menu import Menu
        self.pop_all()
        self.machine.push_later(Menu(self.parent, self.machine))
