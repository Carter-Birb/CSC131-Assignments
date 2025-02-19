
class SaleItem():
    
    def __init__(self, name:str, cost:float, price:float):
        self.name = name
        self.cost = cost
        self.price = price
    
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    
    @property
    def cost(self):
        return self._cost
    
    @cost.setter
    def cost(self, value):
        if value < 0:
            self._cost = 0
        else:
            self._cost = value
    
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            self._price = 0
        else:
            self._price = value
    
    
    def profit(self) -> float:
        return round(float(self.price - self.cost), 2)
    
    
    def apply_sale(self, percentage):
        decimal = percentage / 100
        self.price = round(float(self.price - (self.price * decimal)), 2)
    
    
    def __str__(self):
        return (f"{self.name}\t{self.cost:.2f}\t{self.price:.2f}")


if __name__ == "__main__":
    pass