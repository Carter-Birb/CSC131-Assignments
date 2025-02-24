#####################################################################
# author: Carter Landry
# date: 2/13/25
# description: This is a Card Game containing the Card, Deck, and Game classes.
#####################################################################
# import the shuffle and seed functions from the random library.
from random import randint
import random
import os
# set the seed
random.seed(9876543210)
# define the possible suits that the cards can have using a list.
POSSIBLESUITS = ["clubs", "diamonds", "hearts", "spades"]

# Card class
class Card:
    
    # Constructor for Card
    def __init__(self, number:int, suit:str):
        self.number = number
        self.suit = suit
    
    # Getter for number
    @property
    def number(self):
        return self._number
    
    # Setter for number
    @number.setter
    def number(self, val):
        if val in range(2, 11):
            self._number = val
        else:
            self._number = 2
    
    # Getter for suit
    @property
    def suit(self):
        return self._suit
    
    # Setter for suit
    @suit.setter
    def suit(self, val):
        val = str(val)
        if val.lower() in POSSIBLESUITS:
            self._suit = val.lower()
        else:
            self._suit = "clubs"
    
    # Operation overloader for ">"
    def __gt__(self, other):
        if self.number > other.number:
            return True
        else:
            return False
    
    # Operation overloader for "<"
    def __lt__(self, other):
        if self.number < other.number:
            return True
        else:
            return False
    
    # Operation overloader for "="
    def __eq__(self, other):
        if self.number == other.number:
            return True
        else:
            return False
    
    # Str method for Card
    def __str__(self):
        return f"{self.number}_of_{self.suit}"
    
    # Hash method for Card
    def __hash__(self):
        return hash((self.number, self.suit))


# PictureCard class
class PictureCard(Card):
    
    # Constructor for PictureCard
    def __init__(self, number:int, suit:str):
        super().__init__(number, suit)
        self.imagefile = f"{self.number}_of_{self.suit}.png"
    
    # Getter for imagefile
    @property
    def imagefile(self):
        return self._imagefile
    
    # Setter for imagefile
    @imagefile.setter
    def imagefile(self, val:str):
        
        # Generates the file path
        filepath = os.path.join("images", val)
        
        # Checks if the imagefile is actually a file within the "images" folder
        if os.path.isfile(filepath):
            self._imagefile = val
        else:
            self._imagefile = "default.png"


# Deck class
class Deck:
    
    # Constructor for Deck
    def __init__(self):
        # Generates a list of all possible cards with all possible suits
        self.cards = [PictureCard(number, suit) for suit in POSSIBLESUITS for number in range (2, 11)]

    # Getter for cards
    @property
    def cards(self):
        return self._cards
    
    # Setter for cards
    @cards.setter
    def cards(self, val):
        self._cards = val
    
    # Shuffle function
    def shuffle(self):
        """
        shuffles the cards in the deck.
        """
        random.shuffle(self.cards)
    
    # Size function
    def size(self):
        """
        Returns the size of the deck
        """
        return len(self.cards)
    
    # Draw function
    def draw(self):
        """
        Draws the first card in the deck. (Index 0)
        """
        if len(self.cards) == 0:
            return None
        else:
            drawncard = self.cards[0]
            self.cards.pop(0)
            return drawncard
    
    # Str method for Deck
    def __str__(self):
        if len(self.cards) == 0:
            return "[--empty--]"
        else:
            # Converts the Card objects stored in memory to strings
            return ", ".join(str(card) for card in self.cards)


# Game class
class Game:
    
    # Constructor for Game
    def __init__(self):
        self.start()
    # getter for deck
    @property
    def deck(self):
        return self._deck
    
    # Setter for deck
    @deck.setter
    def deck(self, val):
        self._deck = val
    
    # Start function
    def start(self):
        """
        Initializes the game.
        Normally called when the game first begins, or when the "Restart" button is clicked.
        """
        self.deck:list[Card] = Deck()
        self.deck.shuffle()
        self.deck.shuffle()
        result = "Who wins?"
        return result
    
    # End function
    def end(self):
        """
        Terminates the game.
        Called when the "Quit" button is clicked.
        """
        exit()
    
    # Play function
    def play(self):
        """
        Contains the logic of the game.
        Called when the "Play" button is clicked.
        """
        usercard = self.deck.draw()
        computercard = self.deck.draw()
        
        # Occurs when the deck runs out of cards
        if not usercard or not computercard:
            return None, None, "The deck is empty!"
        
        # The following code checks the value of the cards and executes the required outcome
        elif usercard > computercard:
                result = "You win"
            
        elif computercard > usercard:
                result = "I win"
            
        else:
                result = "Draw"

        return usercard, computercard, result

if __name__ == "__main__":
    pass