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
        productButton = Button(self, text="Exit", command=self.clickProductButton)

        # place button at (0,0)
        productButton.place(x=0, y=0)


    def clickProductButton(self):
        webview.create_window('Hello world', 'https://www.minecraft.net/en-us')
        webview.start()


# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("SmartCue")

# show window
root.mainloop()

