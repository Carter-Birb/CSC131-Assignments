from tkinter import *
from PIL import Image, ImageTk
import backend

WIDTH = 1200
HEIGHT = 850
BGLABEL = "SteelBlue4"
BGBUTTON = "midnight blue"
FONT = "Outfit"

class MainGUI(Frame):
    
    
    def __init__(self, parent):
        super().__init__(parent, bg=BGLABEL)
        self.game = backend.Game()
        self.game.start()
        self.setupGUI()
    
    
    def setupGUI(self):
        """
        Creates the GUI for the Card Game
        """
        # Creates the grid used for placing Labels and Buttons
        for row in range(10):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(50):
            Grid.columnconfigure(self, col, weight=1)
        
        # Creates the center line
        self.canvas = Canvas(
            self,
            height=726,
            width=2,
            bg=BGLABEL,
            highlightthickness=0
        )
        self.canvas.grid(row=5, column=0, columnspan=51, sticky=NSEW, padx=5, pady=5)
        self.canvas.create_line(596, -1000, 596, 1000, fill="gray", width=2)
        
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
        self.Play.grid(row=10, column=0, sticky=W, padx=5, pady=5)
        
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
        self.Restart.grid(row=10, column=1, sticky=W, padx=5, pady=5)
        
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
        self.Quit.grid(row=10, column=50, sticky=E, padx=5, pady=5)
        
        
        # The labels following this comment are meant to change based on the state of the game #
        
        # Creates the Label that displays information about the current game state or winner
        self.status = Label(
            self,
            text="Who wins?",
            anchor=CENTER,
            bg=BGLABEL,
            fg="white",
            font=(FONT, 15)
        )
        self.status.grid(row=8, column=0, columnspan=51, sticky=NSEW, padx=5, pady=5)
        
        # Establishes the default image to show when the GUI begins
        self.defaultimage = PhotoImage(file="images/default.png")
        
        # Creates a variable to store the current image displayed
        self.computercardimage = self.defaultimage
        self.computerimage = Label(
            self,
            image=self.computercardimage,
            width=500,
            height=726,
            bg=BGLABEL
            )
        self.computerimage.grid(row=5, column=0, columnspan=20, sticky=E, padx=5, pady=5)
        
        # Creates a variable to store the current image displayed
        self.usercardimage = self.defaultimage
        self.userimage = Label(
            self,
            image=self.usercardimage,
            width=500,
            height=726,
            bg=BGLABEL
        )
        self.userimage.grid(row=5, column=31, columnspan=20, sticky=W, padx=5, pady=5)

        self.pack(fill=BOTH, expand=True)
    
    
    def process(self, button):
        if button == "Play":
            usercard, computercard, result = self.game.play()
            
            if usercard and computercard:
                
                self.status.config(text=result)

                usercardimage = PhotoImage(file=f"images/{usercard}.png")
                computercardimage = PhotoImage(file=f"images/{computercard}.png")
                
                self.userimage.config(image=usercardimage)
                self.computerimage.config(image=computercardimage)
                    
                self.userimage.image = usercardimage
                self.computerimage.image = computercardimage
                

            else:
                self.status.config(text="Game Over. Restart to play again.")
        
        
        elif button == "Restart":
            result = self.game.start()
            userdefault = PhotoImage(file="images/default.png")
            computerdefault = PhotoImage(file="images/default.png")
            
            self.userimage.config(image=userdefault)
            self.computerimage.config(image=computerdefault)
            
            self.userimage.image = userdefault
            self.computerimage.image = computerdefault
            
            self.status.config(text=result)
        
        
        elif button == "Quit":
            self.game.end()


def main():
    window = Tk()
    window.title("Awesome Card Game")
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.resizable(0, 0)
    
    _ = MainGUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()