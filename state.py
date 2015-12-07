import tkinter as tk

class   State(tk.Frame):
    """Base class with basic logic for states"""
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

    """pop this state from the stack"""
    def pop(self):
        self.machine.pop_later(self)

    """pop the whole stack"""
    def pop_all(self):
        self.machine.pop_all_later()

class   Machine(tk.Frame):
    """Container for states with all the logic needed"""
    def __init__(self, parent):
        super().__init__(parent)
        self.states = []
        self.pops = []
        self.pushs = []
    
    """The pop one method"""
    def pop_later(self, state):
        self.pops.append(state)

    """The pop all method"""
    def pop_all_later(self):
        for i in reversed(self.states):
            self.pops.append(i)

    "To add a state to the top of the stack"""
    def push_later(self, state):
        self.pushs.append(state)

    """Helper function, do not use"""
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

    """Helper function, do not use"""
    def _push(self, state):
        try:
            self.states[-1].hide()
        except:
            pass
        self.states.append(state)
        self.states[-1].focus()
        self.states[-1].unhide()

    """Update the top state then updates the stack"""
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

    """Show the top state"""
    def show(self):
        if len(self.states) == 0:
            return
        self.states[-1].show()

    "Helper function to know if the stack is empty or not (empty == end of program)"""
    def isEmpty(self):
        return len(self.states) == 0
