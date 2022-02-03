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
        

       
               
class NewWindow(Toplevel):
     
    def __init__(self, master = None):
         
        super().__init__(master = master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text ="This is a new Window")
        label.pack()

    


# initialize tkinter
root = Tk()
app = Window(root)
workplace = NewWindow(app)

root.mainloop()

