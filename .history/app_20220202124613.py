import webview
import tkinter
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
      
        self.pack()
     

        self.productInput = Entry(self, bd = 5)
        self.productInput.pack(side = TOP)
        
        

        self.productButton = Button(self, text="Product", command=self.clickProductButton)
        self.productButton.pack(side = BOTTOM)


    def clickProductButton(self):
        webview.create_window('Hello world', 'https://www.minecraft.net/en-us')
        webview.start()

    


# initialize tkinter
root = Tk()
app = Window(root)

root.mainloop()

