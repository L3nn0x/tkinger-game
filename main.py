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
		self.filemenu.add_command(label="New", command=self.new)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit", command=self.win.destroy)
		self.helpmenu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)
		self.helpmenu.add_command(label="About", command=self.about)		
		self.win.config(menu=self.menubar)
		self.map = Canvas(self.win, width=500, height=500)
		self.map.pack()
		#Dimensions
		self.win.geometry('640x480')
		self.win.minsize(width=212,height=134)

	def run(self):
		self.win.mainloop()		
	
	def new(self):
		pass
	
	def about(self):
		showinfo('Information sur le programme','v0.1, PA10')

	def update(self):
		try:
			self.map.update(134)
		except ValueError:
			showinfo("Youuuuu WIN !")
		except KeyError:
			showerror("You're dead, bitch !")

		self.map.show()
		self.win.after(134, update)


main = Main()
main.run()
