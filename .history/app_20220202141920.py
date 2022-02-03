import webview
import tkinter
from tkinter import *

from tkinter import *
from tkinter.ttk import *
 
 
class NewWindow(Toplevel):
     
    def __init__(self, master = None, url = None):
         
        super().__init__(master = master, url = None)
        self.title("New Window")
        self.geometry("200x200")
        self.url = url
        label = Label(self, text ="This is a new Window")
        project = Button(self, text = "Open Project", command = self.openProject)
        label.pack()
        project.pack()
    
    def openProject(self):
        webview.create_window('Hello Project', self.url)
        webview.start()
 
# creates a Tk() object
master = Tk()
 
# sets the geometry of
# main root window
master.geometry("200x200")
 
label = Label(master, text ="This is the main window")
label.pack(side = TOP, pady = 10)
 
# a button widget which will
# open a new window on button click
btn = Button(master,
             text ="Click to open a new window")
 
# Following line will bind click event
# On any click left / right button
# of mouse a new window will be opened



btn.bind("<Button>",
         lambda e: NewWindow(master, 'https://www.youtube.com/'))

 
btn.pack(pady = 10)
 
# mainloop, runs infinitely
mainloop()

