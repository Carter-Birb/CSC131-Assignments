# Carter Landry
# 2/5/25
# Calculator GUI that barely works (It works much better now that I've updated it in Pi Activity 3)
# This program will generate a GUI that resembles a functioning calculator

from tkinter import *
from button_data import button_data_for_assignment

WIDTH = 400
HEIGHT = 650


# The GUI
class MainGUI(Frame):
    # This variable is used to determine whether or not the display will reset when pressing a new button
    RESET = False
    
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.setupGUI()
    
    
    def setupGUI(self):
        
        # The top display
        self.display = Label(
            self,
            text="",
            anchor=E,
            bg="white",
            fg="black",
            height=1,
            font=("Comic Sans MS", 50)
            )
        self.display.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        
        # Configure the grid
        for row in range(6):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)
        
        for button in button_data_for_assignment:
            if button['row'] == 6 and button['col'] == 1 and button['value'] == ' ':
                pass
            else:
                self.makebutton(
                    button['row'],  # button.get("row")
                    button['col'],
                    button['value']
                    )
        
        self.pack(fill=BOTH, expand=1)
    
    
    def makebutton(self, row, col, value):
        bgcolor = "#dddddd"
        # This variable is used to determine the span for each button
        span = 1
        if value == "=":
            bgcolor = "blue"
            # The span is changed for the "=" button to fit the bottom of the calculator
            span = 2
        
        elif value in ["(", ")", "AC", "**", "+", "-", "*", "/", "←", "%"]:
            bgcolor = "#999999"
        
        button = Button(
            self,
            font=("Comic Sans MS", 28),
            text=value,
            fg="black",
            bg=bgcolor,
            highlightbackground=bgcolor, # Needed for macOS (Your grader's PC)
            borderwidth=0,
            highlightthickness=0,
            width=5,
            activebackground="white",
            command=lambda: self.process(value)
        )
        
        button.grid(row=row, column=col, sticky=NSEW, columnspan=span)
    
    
    def process(self, button):
        """
        param 'button' represents the value on the button
        ex: '=' to evaluate, '+' for addition
        """
        if button == "AC":
            # Clear the display
            self.display['text'] = ""
            
        elif button == "=":
            expr = self.display['text']
            
            try:
                result = str(eval(expr))
                # Truncates the result if it exceeds 14 characters
                if len(result) > 14:
                    self.display['text'] = result[:-4] + "..."
                    # Sets reset to true, meaning the next button pressed will reset the display
                    MainGUI.RESET = True
                    
                else:
                    self.display['text'] = result
                    # Sets reset to true, meaning the next button pressed will reset the display
                    MainGUI.RESET = True
                    
            except:
                self.display['text'] = "ERROR"
                # Sets reset to true, meaning the next button pressed will reset the display
                MainGUI.RESET = True
                
        # Handles the back button to remove the last character
        elif button == "←":
            # If reset is True, the display will reset when pressing a button
            if MainGUI.RESET:
                self.display['text'] = ""
            self.display['text'] = self.display['text'][:-1]
            # Sets reset to False after the next button is pressed
            MainGUI.RESET = False
            
        else:
            # If reset is True, the display will reset when pressing a button
            if MainGUI.RESET:
                self.display['text'] = ""
            # Append the button value to the display
            # This does not allow the user to input more than 14 characters
            if len(self.display['text']) >= 14:
                pass
            
            else:
                self.display['text'] += button
            # Sets reset to False after the next button is pressed
            MainGUI.RESET = False


# Main
window = Tk()
window.title("Silly Calculator That Barely Works")
window.geometry(f"{WIDTH}x{HEIGHT}")

p = MainGUI(window)
window.mainloop()