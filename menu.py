import tkinter as tk
from state import State
from game import Game

class   Menu(State):
    def __init__(self, parent, machine):
        super().__init__(parent, machine)
        self.initUI()

    def initUI(self):
        self.playButton = tk.Button(self, text="Play THE Game", command=self.launch)
        self.quitButton = tk.Button(self, text="Quit THE Game (sniff)", command=self.quit)
        self.playButton.pack()
        self.quitButton.pack()

    def launch(self):
        self.machine.push_later(Game(self.parent, self.machine))

    def quit(self):
        self.pop()

    def update(self, dt):
        pass
