import webview
import tkinter

from tkinter import *

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

    productLaunch = Button(self, text = "")

# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("SmartCue")

# show window
root.mainloop()

