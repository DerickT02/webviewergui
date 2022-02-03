import webview
import selenium
from tkinter import *
from selenium import webdriver

from tkinter import *
from tkinter.ttk import *
 
PATH = "/Users/Aldrick/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)

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
        driver.get(self.url)
 

master = Tk()

master.geometry("200x200")
 
label = Label(master, text ="This is the main window")
label.pack(side = TOP, pady = 10)
 



btn = Button(master,
             text ="Click to open a new window")
 
# Following line will bind click event
# On any click left / right button
# of mouse a new window will be opened



btn.bind("<Button>",
         lambda e: NewWindow(master, 'https://www.youtube.com/watch?v=Xjv1sY630Uc'))

 
btn.pack(pady = 10)
 
# mainloop, runs infinitely
mainloop()

