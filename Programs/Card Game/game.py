from tkinter import *
import Game_backend

WIDTH = 700
HEIGHT = 600
BGLABEL = "SteelBlue4"
BGBUTTON = "midnight blue"
FONT = "Outfit"

class MainGUI(Frame):
    
    
    def __init__(self, parent):
        super().__init__(parent, bg=BGLABEL)
        self.setupGUI()
    
    
    def setupGUI(self):
        """
        Creates the GUI for the Card Game
        """
        # Creates the center line
        self.canvas = Canvas(
            self,
            height=450,
            width=250,
            bg=BGLABEL,
            highlightthickness=0
        )
        self.canvas.grid(row=5, column=25, sticky=NSEW, padx=5, pady=5)
        self.canvas.create_line(125, -1000, 125, 1000, fill="gray", width=2)
        
        # Creates the "Computer Picked" Label
        self.L1 = Label(
            self,
            text="Computer Picked",
            anchor=NW,
            bg=BGLABEL,
            fg="white",
            font=(FONT, 12)
            )
        self.L1.grid(row=0, column=0, columnspan=2, sticky=NW, padx=5, pady=5)
        
        # Creates the "You picked" Label
        self.L2 = Label(
            self,
            text="You picked",
            anchor=NE,
            bg=BGLABEL,
            fg="white",
            font=(FONT, 12)
        )
        self.L2.grid(row=0, column=50, sticky=NE, padx=5, pady=5)
        
        # Creates the "Play" Button and activates the process when clicked
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
        
        # Creates the "Restart" Button and activates the process when clicked
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
        
        # Creates the "Quit" Button and activates the process when clicked
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
        self.Quit.grid(row=10, column=50, sticky=SE, padx=5, pady=5)
        
        
        # The labels following this comment are meant to change based on the state of the game #
        
        # Creates the Label that displays the winner of each round
        self.status = Label(
            self,
            text="Who wins?",
            anchor=CENTER,
            bg=BGLABEL,
            fg="white",
            font=(FONT, 15)
        )
        self.status.grid(row=9, column=25, sticky=NSEW, padx=5, pady=5)
        
        
        # Creates the grid used for placing Labels and Buttons
        for row in range(10):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(50):
            Grid.columnconfigure(self, col, weight=1)
        self.pack(fill=BOTH, expand=True)
    
    
    def process(self, button):
        if button == "Play":
            pass


if __name__ == "__main__":#
    window = Tk()
    window.title("Awesome Card Game")
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.resizable(0, 0)
    
    p = MainGUI(window)
    window.mainloop()