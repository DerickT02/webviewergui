import webview
import tkinter

from tkinter import *

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        productButton = Button(self, text="Product", command=self.clickProductButton)

        # place button at (0,0)
        productButton.place(x=0, y=0)


    def clickProductButton(self):
        webview.create_window('Hello world', 'https://www.minecraft.net/en-us')
        webview.start()


# initialize tkinter
root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.mainloop()

