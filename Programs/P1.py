# Name: Carter Landry
# Date: 12/16/24
# Description: This file will read a file given by the user and identify 
            # the amount of times a string the user provides
            # is present within said file.


# User defined functions (including a function called main)

def readFile(filename:str):
    
    while True:
        
        try:
            
            with open(filename) as file:
                filecontents = file.read()
                break
        
        except FileNotFoundError:
            filename = input("That file does not exist, please enter a valid file.\n")
    
    cleanfile = filecontents.replace(" ", "")
    
    return list(cleanfile.splitlines())


def beginswith(filestr:str, userstr:str) -> bool:
    
    return filestr.startswith(userstr)


def endswith(filestr:str, userstr:str) -> bool:
    
    return filestr.endswith(userstr)


def contains(filestr:str, userstr:str) -> bool:
    
    return userstr in filestr


def getStats(names:list, substr:str) -> str:
    
    start = 0
    end = 0
    occur = 0
    
    for i in range(0, len(names)):
        
        name = names[i].lower()
        
        if beginswith(name, substr):
            start += 1
        
        if endswith(name, substr):
            end += 1
        
        if contains(name, substr):
            occur += 1
    
    return [start, end, occur]


def main():

    filename = str(input("Which file would you like to open?\n"))
    
    file = readFile(filename)
    
    totalnames = len(file)
    
    print(f"the file has {totalnames} names in it")
    
    substring = str(input("What name (or substring) are you looking for?\n")).lower()
    
    stats = getStats(file, substring)
    
    startcount = stats[0]
    endcount = stats[1]
    contains = stats[2]
    
    print(30 * "-")
    print(f"{startcount} names start with this string")
    print(f"{endcount} names end with this string")
    print(f"{contains} names contain this string")
    print(30 * "-")


if __name__ == "__main__":
    main()