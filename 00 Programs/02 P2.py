# Name: Carter Landry
# Date: 1/7/25
# Description: This file will take the population values from a file and ask the user for a
# minimum, maximum, and amount of rows they wish for their table to contain. The code will then
# provide a list of population values based on the user's input and provide the frequency of a certain
# population value within the file.



##### FUNCTIONS #####



def load_file(filename: str):
    """
    Opens the file and converts it to a list of integers for processing.
    """
    while True:
        
        # Attempts to open the file the user has provided except when the file does not exist.
        try:
            
            with open(filename) as file:
                filecontents = file.read()
                listfilecontents = filecontents.splitlines()
                break
        
        except FileNotFoundError:
            filename = input("That file does not exist, please enter a valid file.\n")
    
    # Converts the file contents from a list of strings to a list of integers.
    intfilecontents = [int(population) for population in listfilecontents]
    
    return intfilecontents


def create_ranges(min: int, max: int, rows: int):
    """
    Generates a list of ranges given by the user.
    """
    i = 0
    ranges = []
    
    diffmaxmin = max - min
    
    baserange = diffmaxmin / rows
    
    while i < rows:
        
        # Adds a value to the list based on the user's min and max, and repeats this depending on the amount of rows stated.
        ranges.append(f"{int((i * baserange) + min)} - {int((((i + 1) * baserange) - 1) + min)}")
        i += 1
    
    return ranges


def count_cities(ranges: list, populations: list):
    """
    Counts the frequency of a population value occuring within the ranges provided.
    """
    frequencies = []
    
    for range in ranges:
        
        frequency = 0
        
        # Cleans the list generated to only contain the two range values aswell as converts the values from strings to integers
        values:list = range.split()
        values.remove("-")
        intvalues = [int(value) for value in values ]

        for population in populations:
            
            # Checks if a value within the list of populations is within a range within the list of ranges.
            if intvalues[0] <= population <= intvalues[1]:
                
                frequency += 1
    
        frequencies.append(frequency)
    
    return frequencies
    


def generate_table(popranges: list, frequencies: list):
    """
    Generates a table for the user.
    """
    Population = "Population"
    Frequencies = "Frequencies"
    dashes = "-" * 40
    tableheader = f"{Population:<{23}}{Frequencies:<{17}}"
    data = []
    
    # Converts the integer lists to string lists
    strfrequencies = [str(frequency) for frequency in frequencies]
    strpopranges = [str(poprange) for poprange in popranges]
    
    for i in range(len(strfrequencies)):
        
        temp = strpopranges[i] + "\t\t" + strfrequencies[i]
        data.append(temp)
        
    unpackeddata = "\n".join(data)
    
    return f"{dashes}\n{tableheader}\n{dashes}\n{unpackeddata}\n{dashes}"
    


def main():
    """
    Main
    """
    filename = input("What is the name of the file with the population information? ")
    
    populations = load_file(filename)
    
    totalpops = len(populations)
    
    print(f"This file has {totalpops} cities it.")
    
    min = int(input("What population would you like to set as the minimum? "))
    max = int(input("What population would you like to set as the maximum? "))
    rows = int(input("How many rows to you want in your table? "))
    
    ranges = create_ranges(min, max, rows)
    
    frequencies = count_cities(ranges, populations)
    
    print(generate_table(ranges, frequencies))



##### MAIN #####



if __name__ == "__main__":
    main()