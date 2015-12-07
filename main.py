from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror
from map import *


class Main():
	def __init__(self):
            #Déclaration de la fenetre
            self.win = Tk()
            self.win.title('THE game')
            #Menus
            self.menubar = Menu(self.win)
            self.filemenu = Menu(self.menubar, tearoff=0)
            self.menubar.add_cascade(label="File", menu=self.filemenu)
            self.filemenu.add_command(label="New game", command=self.new)
            self.filemenu.add_command(label="Open level", command=self.new)
            self.filemenu.add_separator()
            self.filemenu.add_command(label="Exit", command=self.win.destroy)
            self.helpmenu = Menu(self.menubar, tearoff=0)
            self.menubar.add_cascade(label="Help", menu=self.helpmenu)
            self.helpmenu.add_command(label="About", command=self.about)		
            self.win.config(menu=self.menubar)
            self.new()
            #Dimensions
            self.win.geometry('500x500')
            self.win.minsize(width=500,height=500)
            self.win.maxsize(width=500, height=500)

	def run(self):
            self.update()
            self.win.mainloop()		
	
	def new(self, level = 1):
            self.level = level
            filename = "Levels/niveau" + str(level) + ".txt"
            try:
                self.map.load(filename)
            except AttributeError:
                self.map = Map(self.win, filename, width=500, height=500)
                self.map.pack()
                self.map.focus_set()
	
	def about(self):
		showinfo('Information sur le programme','v0.1, PA10')

	def update(self):
            try:
                self.map.update(33) #frequence de rafraichissement
            except KeyError:
                level = self.level + 1
                showinfo("THE Game", "Youuuuu WIN ! Next level : " + str(level))
                self.new(level)
            except ValueError:
                showerror("THE Game", "You're dead, bitch !")
                exit(0)

            self.map.show()
            self.win.after(33, self.update)


main = Main()
main.run()
