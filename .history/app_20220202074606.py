import webview
import tkinter

from tkinter import *

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack()
     

        productInput = Entry(self, bd = 5)
        productInput.pack(side = TOP)
        productName = productInput.get()
        print(productName)

        productButton = Button(self, text="Product", command=self.clickProductButton)
        productButton.pack(side = BOTTOM)


    def clickProductButton(self):
        webview.create_window('Hello world', 'https://www.minecraft.net/en-us')
        webview.start()


# initialize tkinter
root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.mainloop()

