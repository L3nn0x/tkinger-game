import tkinter as tk

class   State(tk.Frame):
    def __init__(self, parent, machine):
        super().__init__(parent)
        self.parent = parent
        self.machine = machine

    def update(self, dt):
        pass

    def hide(self):
        self.pack_forget()

    def unhide(self):
        self.pack(fill=tk.BOTH, expand=tk.YES)

    def show(self):
        pass

    def pop(self):
        self.machine.pop_later(self)

    def pop_all(self):
        self.machine.pop_all_later()

class   Machine(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.states = []
        self.pops = []
        self.pushs = []
    
    def pop_later(self, state):
        self.pops.append(state)

    def pop_all_later(self):
        for i in reversed(self.states):
            self.pops.append(i)

    def push_later(self, state):
        self.pushs.append(state)

    def _pop(self, state):
        if len(self.states) == 0:
            return
        if state == self.states[-1]:
            state.hide()
        self.states.pop()
        if len(self.states) == 0:
            return
        self.states[-1].focus()
        self.states[-1].unhide()

    def _push(self, state):
        try:
            self.states[-1].hide()
        except:
            pass
        self.states.append(state)
        self.states[-1].focus()
        self.states[-1].unhide()

    def update(self, dt):
        if len(self.states) == 0:
            return
        self.states[-1].update(dt)
        for i in self.pops:
            self._pop(i)
        for i in self.pushs:
            self._push(i)
        self.pops = []
        self.pushs = []

    def show(self):
        if len(self.states) == 0:
            return
        self.states[-1].show()

    def isEmpty(self):
        return len(self.states) == 0
