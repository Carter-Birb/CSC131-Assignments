
class Room:
    
    # Constructor
    def __init__(self, name:str):
        self.name = name
        self.exitdirections: list[str] = [] # north, south, east, west
        self.exitdestinations: list[Room] = []
        self.items: list[str] = []
        self.itemdescriptions: list[str] = []
        self.lootables: list[str] = []
    
    # Getters / Setters
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) != str:
            raise TypeError("self.name must be a str")
        
        self._name = value
    
    
    @property
    def exitdirections(self):
        return self._exitdirections
    
    @exitdirections.setter
    def exitdirections(self, value: list[str]):
        self._exitdirections = value
    
    
    @property
    def exitdestinations(self):
        return self._exitdestinations
    
    @exitdestinations.setter
    def exitdestinations(self, value: list['Room']):
        self._exitdestinations = value
    
    
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, value: list[str]):
        self._items = value
    
    
    @property
    def itemdescriptions(self):
        return self._itemdescriptions
    
    @itemdescriptions.setter
    def itemdescriptions(self, value: list[str]):
        self._itemdescriptions = value
    
    
    @property
    def lootables(self):
        return self._lootables
    
    @lootables.setter
    def lootables(self, value: list[str]):
        self._lootables = value
    
    
    
    # Additional methods
    
    def addexit(self, exitdirection: str, exitdestination: 'Room'):
        self.exitdirections.append(exitdirection)
        self.exitdestinations.append(exitdestination)
    
    
    def additem(self, itemname: str, itemdescription: str):
        self.items.append(itemname)
        self.itemdescriptions.append(itemdescription)
    
    
    # IMPROVEMENT #
    def deleteitem(self, existingitem: str):
        if existingitem in self.items:
            self.items.remove(existingitem)
    # IMPROVEMENT #
    
    
    def addlootable(self, newlootable: str):
        self.lootables.append(newlootable)
    
    
    def deletelootable(self, existinglootable: str):
        if existinglootable in self.lootables:
            self.lootables.remove(existinglootable)
    
    
    # __str__ method for conversion to a string
    
    def __str__(self):
        result = []
        
        # Where we are
        result.append(f"Location: {self.name}")
        
        # What we see
        if len(self.items) != 0:
            result.append("You see: ")
            for item in self.items:
                result.append(f"- {item}")
        
        # Exits
        if len(self.exitdirections) != 0:
            result.append("Exits:")
            for direction in self.exitdirections:
                result.append(f"- {direction}")
        
        result = "\n".join(result)
        return result



if __name__ == "__main__":
    
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    
    r1.addexit("East", r2)
    r1.additem("Chair", "It is made of wicker.")
    r1.addlootable("Key")
    r1.deletelootable("Key")
    
    print(r1)