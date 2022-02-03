import webview
import tkinter

from tkinter import *

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack()

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)

        # place button at (0,0)
        exitButton.place(x=0, y=0)


# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("SmartCue")

# show window
root.mainloop()

