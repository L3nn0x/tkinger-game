from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror
from state import Machine
from menu import Menu as MenuState
from glob import X, Y

class Main():
	def __init__(self):
            #Déclaration de la fenetre
            self.win = Tk()
            self.win.title('THE game')
            #Menus
            self.menubar = Menu(self.win)
            self.filemenu = Menu(self.menubar, tearoff=0)
            self.menubar.add_cascade(label="File", menu=self.filemenu)
            # self.filemenu.add_command(label="New game", command=self.new)
            # self.filemenu.add_command(label="Open level", command=self.new)
            self.filemenu.add_separator()
            self.filemenu.add_command(label="Exit", command=self.win.destroy)
            self.helpmenu = Menu(self.menubar, tearoff=0)
            self.menubar.add_cascade(label="Help", menu=self.helpmenu)
            self.helpmenu.add_command(label="About", command=self.about)		
            self.win.config(menu=self.menubar)
            self.machine = Machine(self.win)
            self.machine._push(MenuState(self.win, self.machine))
            #Dimensions
            self.win.geometry(str(X)+'x'+str(Y))

	def run(self):
            self.update()
            self.win.mainloop()		
	
	def about(self):
		showinfo('Information sur le programme','v0.1, PA10')

	def update(self):
            self.machine.update(33)
            self.machine.show()
            if self.machine.isEmpty():
                self.win.destroy()
            self.win.after(33, self.update)


main = Main()
main.run()
