from tkinter import *




class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master


        self.pack(fill=BOTH, expand=1)
        exitbutton = Button(self, text = "Log out", command = self.clickExitButton)
        exitbutton.place(x=50, y=50)

    def clickExitButton(self):
            exit()

    
window = Tk()
app = Window(window)
window.wm_title("Window")
window.geometry("300x700")
window.mainloop()
