# Carter Landry
# 2/5/25
# This is an extension of the SaleItem class.

# This is the SaleItem class
class SaleItem():
    # Constructor for SaleItem
    def __init__(self, name:str, cost:float, price:float):
        self.name = name
        self.cost = cost
        self.price = price
    
    # Getter for name
    @property
    def name(self):
        return self._name
    # Setter for name
    @name.setter
    def name(self, value):
        self._name = value
    
    # Getter for cost
    @property
    def cost(self):
        return self._cost
    # Setter for cost
    @cost.setter
    def cost(self, value):
        if value < 0:
            self._cost = 0
        else:
            self._cost = value
    
    # Getter for price
    @property
    def price(self):
        return self._price
    # Setter for price
    @price.setter
    def price(self, value):
        if value < 0:
            self._price = 0
        else:
            self._price = value
    
    # Profit function (returns profit)
    def profit(self):
        """
        returns the total profit of a SaleItem
        """
        return round(float(self.price - self.cost), 2)
    
    # apply_sale function (returns price after a sale is applied)
    def apply_sale(self, percentage):
        """
        returns the price after a sale is applied to a SaleItem
        """
        decimal = percentage / 100
        self.price = round(float(self.price - (self.price * decimal)), 2)
    
    # str method for SaleItem class
    def __str__(self):
        return (f"{self.name}\t{self.cost:.2f}\t{self.price:.2f}")

# Clothing class (is a SaleItem)
class Clothing(SaleItem):
    # Constructor for Clothing
    def __init__(self, name:str, brand:str, cost:float, price:float, size:str):
        super().__init__(name, cost, price)
        self.brand = brand
        self.size = size
    
    # Getter for brand
    @property
    def brand(self):
        return self._brand
    # Setter for brand
    @brand.setter
    def brand(self, value):
        self._brand = value
    
    # Getter for size
    @property
    def size(self):
        return self._size
    # Setter for size
    @size.setter
    def size(self, value):
        # Checks if the size is "Small", "Medium", or "Large"
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        # If the value is none of those, the size is set to None
        else:
            self._size = None
    
    # str method for Clothing class
    def __str__(self):
        return (f"{super().__str__()}\t{self.brand}\t{self.size}")

# Food class (is a SaleItem)
class Food(SaleItem):
    # Constructor for Food 
    def __init__(self, name:str, cost:float, price:float):
        super().__init__(name, cost, price)
        self.shelf_life = 7
    
    # Getter for shelf_life
    @property
    def shelf_life(self):
        return self._shelf_life
    # Setter for shelf_life
    @shelf_life.setter
    def shelf_life(self, value):
        # If the value is below 0, it is set to 0
        if value < 0:
            self._shelf_life = 0
        else:
            self._shelf_life = value
    
    # str method for Food class
    def __str__(self):
        return (f"{super().__str__()}\t{self.shelf_life}")


# Shoe class (is Clothing)
class Shoe(Clothing):
    # Constructor for Shoe
    def __init__(self, cost, price, size):
        # Sets all choes to the name "Crocs", and the brand "Nike"
        super().__init__("Crocs", "Nike", cost, price, size)


# Chip class (is Food)
class Chip(Food):
    # Constructor for Chip
    def __init__(self):
        # Sets all chips to the name "Original", cost of 2, price of 3.50, and shelf_life of 21
        super().__init__("Original", 2, 3.50)
        self.shelf_life = 21


# MAIN #
if __name__ == "__main__":
    print(issubclass(Shoe, Clothing))
    
    croc = Shoe(29.99, 229.99, "Medium")
    
    print(croc.name)
    print(croc.brand)
    