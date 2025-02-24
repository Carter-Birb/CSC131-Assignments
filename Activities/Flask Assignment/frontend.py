from time import sleep
import requests
import backend

class Pokedex:
    
    IP_ADDR = "127.0.0.1"
    API_URL = f"http://{IP_ADDR}:8000"
    
    def __init__(self):
        pokedexlist = requests.get(url=f"{Pokedex.API_URL}/pokedexlist")
        self.pokedexlistdata = pokedexlist.json()
    
    
    def startdex(self):
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
    
    
    def getentry(self, pokemon):
            entry = requests.get(url=f"{Pokedex.API_URL}/{pokemon}")
            entrydata = entry.json()
            return f"\nName: {entrydata['name']}\nType: {entrydata['type']}\nWeakness: {entrydata['weakness']}\nRegion: {entrydata['region']}\nDescription: {entrydata['description']}\n"
    
    
    def rundex(self):
        while True:
            userinput = input("").lower().strip()
            
            if userinput in self.pokedexlistdata:
                print(Pokedex.getentry(self, userinput))
                sleep(1)
                
            elif userinput == "entries":
                print("The current Pokemon in the Pokedex are:")
                sleep(1)
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