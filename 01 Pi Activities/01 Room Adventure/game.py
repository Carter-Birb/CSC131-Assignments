from room import Room
from time import sleep

# Creats the rooms globally to be accessed by other functions

# IMPROVEMENT #
r1 = Room("Office")
r2 = Room("Bedroom")
r3 = Room("Bathroom")
r4 = Room("Workshop")
# IMPROVEMENT #

class Game:
    
    def __init__(self):
        self.inventory = []
        self.currentroom = None
        self.response = ""
        self.running = True
        self.createinstance()
    
    def createinstance(self):
        """
        Creates the rooms that exist in the game.
        """
        
        # IMPROVEMENT #
        # Add exits to the rooms
        r1.addexit("north", r2)
        
        r2.addexit("south", r1)
        r2.addexit("east", r3)
        r2.addexit("west", r4)
        
        r3.addexit("west", r2)
        
        r4.addexit("east", r2)
        
        
        # Add items
        r1.additem("door", "It locked behind you when you decided to walk in.")
        r1.additem("chair", "It's an old rocking chair with a rotting cushion on it.")
        r1.additem("tv", "The glass screen is shattered.")
        r1.additem("bookshelf", "It's very dusty, but there's some old books in here.")
        
        r2.additem("bed", "The sheets are gone, and it has a human-shaped stain on it.")
        r2.additem("dresser", "The drawers are empty.")
        r2.additem("mirror", "It's you!")
        
        r3.additem("bathtub", "There's sediment and rust near the drain.")
        r3.additem("cabinet", "There's nothing in here, wait... There's a key.")
        r3.additem("toilet", "The lid is closed, I'm not opening it.")
        
        r4.additem("chainsaw", "There's no gas inside.")
        r4.additem("toolbox", "There's some old tools inside.")
        
        # Add lootables to rooms
        r3.addlootable("key")
        
        self.currentroom = r1
        # IMPROVEMENT #
    
    
    def play(self):
        
        print("You and some friends decided to investigate an abandoned house in your neighborhood.")
        sleep(2)
        print("Little did you know, this would be the last time you'd see your friends again.")
        sleep(2)
        print("You walk into a room when suddenly, the door slams shut behind you, separating you from your friends.")
        sleep(2)
        print("You are now trapped within the house, with no way of knowing where you are.")
        sleep(2)
        
        while self.running:
            if self.currentroom == None:
                self.death()
                break
            
            # Add room info to the status
            status = "\n" + str(self.currentroom)
            
            # Add inventory info to the status
            if len(self.inventory) != 0:
                status += f"\n You are carrying: "
                status += ", ".join(self.inventory)
            
            else:
                status += "\nYou have no items in your inventory."
            
            # Inform the user of the current game status
            print(status)
            
            # Set the default response for the action the user takes
            self.response = "Invalid input. Try the format [verb] [noun]. I only understand the verbs 'go', 'look', and 'take'. Type 'quit' to exit the game."
            
            sleep(1)
            
            # Does the user want to quit?
            action = input("What do you want to do?\n").lower().strip()
            if action in ["quit", "q", "exit", "bye", "see ya", "ciao"]:
                self.running = False
                break
            
            # Interpret the input
            words = action.split()
            if len(words) == 2:
                verb = words[0]
                noun = words[1]
                
                if verb == "go":
                    self.handlego(noun)
                
                elif verb == "look":
                    self.handlelook(noun)
                
                elif verb == "take":
                    self.handletake(noun)
            
            
            # IMPROVEMENT #
            if noun == "cabinet":
                self.addnewitem(r3, "key", "It's old and rusty.")
            # IMPROVEMENT #
            
            
            print(self.response)
            sleep(1)
    
    
    def handlego(self, noun):
        self.response = "Invalid exit."
        if noun in self.currentroom.exitdirections:
            index = self.currentroom.exitdirections.index(noun)
            self.currentroom = self.currentroom.exitdestinations[index]
            self.response = "You moved rooms."
    
    
    def handlelook(self, noun):
        self.response = "That item does not exist here."
        if noun in self.currentroom.items:
            index = self.currentroom.items.index(noun)
            self.response = self.currentroom.itemdescriptions[index]
    
    
    def handletake(self, noun):
        self.response = "That is not something I can take."
        if noun in self.currentroom.lootables:
            self.inventory.append(noun)
            self.currentroom.deletelootable(noun)
            
            
            # IMPROVEMENT #
            self.currentroom.deleteitem(noun)
            # IMPROVEMENT #
            
            
            self.response = f"Picked up {noun}."
    
    
    # IMPROVEMENT
    def addnewitem(self, room: Room, itemname: str, itemdescription: str):
        room.additem(f"{itemname}", f"{itemdescription}")
    # IMPROVEMENT #
    
    
    def death(self):
        print("😁 YOU DIED 😁")
        self.running = False




if __name__ == "__main__":
    pass