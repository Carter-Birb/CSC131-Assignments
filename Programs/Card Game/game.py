from tkinter import *
import CardGame

WIDTH = 600
HEIGHT = 600
BG = "cadet blue"
FONT = "Outfit"

class MainGUI(Frame):
    
    
    def __init__(self, parent):
        super().__init__(parent, bg=BG)
        self.setupGUI()
    
    
    def setupGUI(self):

        self.L1 = Label(
            self,
            text="Computer Picked",
            anchor=NW,
            bg=BG,
            fg="white",
            font=(FONT, 10)
            )
        self.L1.grid(row=0, column=0, sticky=NW)
        
        self.L2 = Label(
            self,
            text="You picked",
            anchor=NE,
            bg=BG,
            fg="white",
            font=(FONT, 10)
        )
        self.L2.grid(row=0, column=6, sticky=NE)
        
        for row in range(4):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(6):
            Grid.columnconfigure(self, col, weight=1)
        
        self.pack(fill=BOTH, expand=1)
    
    
    def process(self, button):
        pass


if __name__ == "__main__":
    window = Tk()
    window.title("Awesome Card Game")
    window.geometry(f"{WIDTH}x{HEIGHT}")
    
    p = MainGUI(window)
    window.mainloop()