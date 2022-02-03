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
        webview.create_window('Hello world', 'https://www.minecraft.net/en-us', confirm_close = True)
        webview.start()
        newWindow = Toplevel(self.master)
        newWindow.title("New Window")


       
               
class Presentation(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        master.title("Presentation")
        self.pack()

    


# initialize tkinter
root = Tk()
app = Window(root)

root.mainloop()

