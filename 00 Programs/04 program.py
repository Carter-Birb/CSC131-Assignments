# Carter Landry
# 1/24/25
# This is a file containing the Height() class which will convert two values (feet, inches) into a value of height of the form [feet' inches"].
# There are also functions within this class that can convert the height to inches, aswell as add, subtract, and compare height values of this form.

class Height():
    
    
    # Constructor
    def __init__(self, ft=0, inch=0):
        self.ft = ft
        self.inch = inch
    
    
    # Getter for feet
    @property
    def ft(self):
        return self._ft
    
    
    # Setter for feet
    @ft.setter
    def ft(self, value):
        if value < 0:
            self._ft = 0
        else:
            self._ft = value
    
    
    # Getter for inches
    @property
    def inch(self):
        return self._inch
    
    
    # Setter for inches
    @inch.setter
    def inch(self, value):
        if value < 0:
            self._inch = 0
        else:
            self._inch = value % 12
            self._ft += value // 12
    
    
    # returns the total inches value of a Height Object
    def inches(self):
        """
        Converts the Height value to pure inches
        """
        return (self.inch + (self.ft * 12))
    
    
    # Operator overload for adding heights
    def __add__(self, other):
        totalfeet = self.ft + other.ft
        totalinch = self.inch + other.inch
        if self.inch >= 12:
            totalfeet = totalfeet // 12
            totalinch = totalinch % 12
        return Height(totalfeet, totalinch)
    
    
    # Operator overload for subtracting heights
    def __sub__(self, other):
        totalfeet = self.ft - other.ft
        totalinch = self.inch - other.inch
        if totalfeet < 0:
            return Height(0, 0)
        else:
            if totalinch < 0:
                totalfeet -= 1
                totalinch += 12
            return Height(totalfeet, totalinch)
    
    
    # Operator overload for finding whether or not a height is greater than another
    def __gt__(self, other):
        if self.ft == other.ft:
            if self.inch > other.inch:
                return True
            else:
                return False
        if self.ft > other.ft:
            return True
        else:
            return False
    
    
    # Operator overload for finding whether or not a height is greater than or equal to another
    def __ge__(self, other):
        if self.ft == other.ft:
            if self.inch >= other.inch:
                return True
            else:
                return False
        if self.ft >= other.ft:
            return True
        else:
            return False
    
    
    # Operator overload for finding whether or not a height is less than another
    def __lt__(self, other):
        if self.ft == other.ft:
            if self.inch < other.inch:
                return True
            else:
                return False
        if self.ft < other.ft:
            return True
        else:
            return False
    
    
    # Operator overload for finding whether or not a height is less than or equal to another
    def __le__(self, other):
        if self.ft == other.ft:
            if self.inch <= other.inch:
                return True
            else:
                return False
        if self.ft <= other.ft:
            return True
        else:
            return False
    

    # Operator overload for fidning whether two heights are equal
    def __eq__(self, other):
        if self.ft == other.ft and self.inch == other.inch:
            return True
        else:
            return False
    
    
    # Operator overload for finding whether two heights are not equal
    def __ne__(self, other):
        if self.ft != other.ft or self.inch != other.inch:
            return True
        else:
            return False
    
    
    # String method
    def __str__(self):
        return f"{self.ft}' {self.inch}\""


def main():
    
    # Testing creation and printing of Height objects
    h1 = Height(6, 5)
    h2 = Height(1, 23)
    h3 = Height()
    h4 = Height(4)
    h5 = Height(0, 77)
    h6 = Height(-5, -4)
    print(f"h1 = {h1}")
    print(f"h2 = {h2}")
    print(f"h3 = {h3}")
    print(f"h4 = {h4}")
    print(f"h5 = {h5}")
    print(f"h6 = {h6}")
    print("=" * 40)

    # Testing inches function
    print(f"{h1} is in fact {h1.inches()} inches")
    print(f"{h3} is in fact {h3.inches()} inches")
    print(f"{h5} is in fact {h5.inches()} inches")
    print("=" * 40)

    # Testing addition and subtraction
    h3 = h1 + h2
    h6 = h5 - Height(4, 10)
    h7 = h4 - h5
    h8 = h1 + Height(0, 1)
    h9 = Height(2, 10)
    print(f"{h1} + {h2} = {h3}")
    print(f"{h5} - {Height(4, 10)} = {h6}")
    print(f"{h4} - {h5} = {h7}")
    print(f"{h1} + {Height(0,1)} = {h8}")
    print("=" * 40)

    # Testing comparison operators
    print(f"{h1} > {h2}: {h1>h2}")
    print(f"{h1} < {h5}: {h1<h5}")
    print(f"{h1} >= {h5}: {h1>=h5}")
    print(f"{h2} <= {h1}: {h2<=h1}")
    print(f"{h3} == {h3}: {h3==h3}")
    print(f"{h1} == {h8}: {h1==h8}")
    print(f"{h1} >= {h8}: {h1>=h8}")
    print(f"{h1} == {h5}: {h1==h5}")
    print(f"{h9} != {h2}: {h9!=h2}")
    print("=" * 40)


# calling the main function above
if __name__ == "__main__":
    main()