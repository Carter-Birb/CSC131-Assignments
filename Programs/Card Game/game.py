from tkinter import *
import CardGame

WIDTH = 600
HEIGHT = 600
BGLABEL = "SteelBlue4"
BGBUTTON = "midnight blue"
FONT = "Outfit"

class MainGUI(Frame):
    
    
    def __init__(self, parent):
        super().__init__(parent, bg=BGLABEL)
        self.setupGUI()
    
    
    def setupGUI(self):

        self.L1 = Label(
            self,
            text="Computer Picked",
            anchor=NW,
            bg=BGLABEL,
            fg="white",
            font=(FONT, 10)
            )
        self.L1.grid(row=0, column=0, sticky=NW, padx=5, pady=5)
        
        self.L2 = Label(
            self,
            text="You picked",
            anchor=NE,
            bg=BGLABEL,
            fg="white",
            font=(FONT, 10)
        )
        self.L2.grid(row=0, column=10, sticky=NE, padx=5, pady=5)
        
        self.Play = Button(
            self,
            text="Play",
            bg=BGBUTTON,
            fg="white",
            highlightbackground=BGBUTTON,
            width=5,
            activebackground="light gray",
            command=lambda: self.process("Play")
        )
        self.Play.grid(row=10, column=0, sticky=SW, padx=5, pady=5)
        
        self.Restart = Button(
            self,
            text="Restart",
            bg=BGBUTTON,
            fg="white",
            highlightbackground=BGBUTTON,
            width=5,
            activebackground="light gray",
            command=lambda: self.process("Restart")
        )
        self.Restart.grid(row=10, column=1, sticky=SW, padx=5, pady=5)
        
        self.Quit = Button(
            self,
            text="Quit",
            bg=BGBUTTON,
            fg="white",
            highlightbackground=BGBUTTON,
            width=5,
            activebackground="light gray",
            command=lambda: self.process("Quit")
        )
        self.Quit.grid(row=10, column=10, sticky=SE, padx=5, pady=5)
        
        
        for row in range(10):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(10):
            Grid.columnconfigure(self, col, weight=1)
        
        self.pack(fill=BOTH, expand=True)
    
    
    def process(self, button):
        pass


if __name__ == "__main__":
    window = Tk()
    window.title("Awesome Card Game")
    window.geometry(f"{WIDTH}x{HEIGHT}")
    
    p = MainGUI(window)
    window.mainloop()