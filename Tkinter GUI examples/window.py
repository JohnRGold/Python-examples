from tkinter import *

class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master

root = Tk()
app = Window(root)

# set window title
root.wm_title("example Tkinter window")

# show window
root.mainloop()
