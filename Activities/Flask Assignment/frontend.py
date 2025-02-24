##########################################
# Carter Landry
# 2/24/25
# This is a Flask Project that uses pokedex entries as endpoints.
##########################################


from time import sleep
import requests
import backend

class Pokedex:

    IP_ADDR = "127.0.0.1"
    API_URL = f"http://{IP_ADDR}:8000"

    def __init__(self):
        # This value is used often in separate functions within the Pokedex class, therefore it is established in the constructor of the Pokedex class
        pokedexlist = requests.get(url=f"{Pokedex.API_URL}/pokedexlist")
        self.pokedexlistdata = pokedexlist.json()


    def startdex(self):
        """
        begins the Pokedex.
        This is only run once when the program starts.
        """
        print("Welcome to the Pokedex!")
        sleep(1)
        print("Valid commands are: \"<pokemon>\" \"entries\" \"help\" \"quit\"")
        sleep(1)
        print("The current Pokemon in the Pokedex are:")
        sleep(1)
        print(", ".join(self.pokedexlistdata))
        sleep(1)
        print("Which pokemon would you like to know more about?")
        Pokedex.rundex(self)


    def getentry(self, pokemon:str):
        """
        returns the formatted pokedex information about a given pokemon.
        """
        entry = requests.get(url=f"{Pokedex.API_URL}/{pokemon}")
        entrydata = entry.json()
        return f"\nName: {entrydata['name'].title()}\nType: {entrydata['type'].title()}\nWeakness: {entrydata['weakness'].title()}\nRegion: {entrydata['region'].title()}\nDescription: {entrydata['description']}\n"


    def rundex(self):
        """
        runs the pokedex
        """
        while True:
            userinput = input("").lower().strip()
            
            if userinput in self.pokedexlistdata:
                # prints the pokedex entry
                print(Pokedex.getentry(self, userinput))
                sleep(1)
                
            elif userinput == "entries":
                print("The current Pokemon in the Pokedex are:")
                sleep(1)
                # Joins the pokemon within the pokedex to a string
                print(", ".join(self.pokedexlistdata))
                sleep(1)
                
            elif userinput == "help":
                print("Valid commands are: \"<pokemon>\" \"entries\" \"help\"")
                sleep(1)
                
            elif userinput == "quit":
                exit()
                
            else:
                print("That pokemon is not in the Pokedex")
                sleep(1)
            
            print("Which pokemon would you like to know more about?")



if __name__ == "__main__":
    p = Pokedex()
    p.startdex()