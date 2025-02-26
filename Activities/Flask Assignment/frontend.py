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
        regions_ = requests.get(url=f"{Pokedex.API_URL}/listregions")
        self.regionsdata = regions_.json()
        self.currentregion = None
        self.currentpokemon = None


    def accessregiondata(self, region:str) -> dict:
        """
        accesses the data contained within a region.
        contains: pokemon
        returns a dictionary.
        """
        regionpokemon = requests.get(url=f"{Pokedex.API_URL}/{region}")
        regiondata = regionpokemon.json()
        return regiondata
    
    def accesspokemondata(self, region:str, pokemon:str) -> dict:
        """
        accesses the data contained within a pokemon.
        contains: pokemon info
        returns a dictionary.
        """
        pokeinfo = requests.get(url=f"{Pokedex.API_URL}/{region}/{pokemon}")
        infodata = pokeinfo.json()
        return infodata
    
    def accessname(self, region:str, pokemon:str) -> dict:
        """
        Accesses the data contained within a pokemon's name.
        Returns a string.
        """
        pokename = requests.get(url=f"{Pokedex.API_URL}/{region}/{pokemon}/name")
        namedata = pokename.json()
        return namedata
    
    def accesstype(self, region:str, pokemon:str) -> dict:
        """
        Accesses the data contained within a pokemon's type.
        Returns a string.
        """
        poketype = requests.get(url=f"{Pokedex.API_URL}/{region}/{pokemon}/type")
        typedata = poketype.json()
        return typedata
    
    def accessweakness(self, region:str, pokemon:str) -> dict:
        """
        Accesses the data contained within a pokemon's weakness.
        Returns a string.
        """
        pokeweakness = requests.get(url=f"{Pokedex.API_URL}/{region}/{pokemon}/weakness")
        weaknessdata = pokeweakness.json()
        return weaknessdata
    
    def accessevolves(self, region:str, pokemon:str) -> dict:
        """
        Accesses the data contained within a pokemon's evolves.
        Returns an integer.
        """
        pokeevolves = requests.get(url=f"{Pokedex.API_URL}/{region}/{pokemon}/evolves")
        evolvesdata = pokeevolves.json()
        return evolvesdata
    
    def accessdescription(self, region:str, pokemon:str) -> dict:
        """
        Accesses the data contained within a pokemon's description.
        Returns a string.
        """
        pokedescription = requests.get(url=f"{Pokedex.API_URL}/{region}/{pokemon}/description")
        descriptiondata = pokedescription.json()
        return descriptiondata
    
    
    
    def regiondir(self, userinput:str) -> dict:
        """
        marks the user's current region location.
        """
        self.currentregion = userinput
    
    def pokemondir(self, region:str, userinput:str) -> dict:
        """
        marks the user's current pokemon location.
        """
        self.currentpokemon = userinput

    
    
    def startdex(self):
        """
        begins the Pokedex.
        This is only run once when the program starts.
        """
        print("Welcome to The Pokedex!")
        sleep(1)
        print("Valid commands are: \"<region>\" \"regions\" \"<pokemon>\" \"pokemon\" \"<data>\" \"back\" \"help\" \"quit\"")
        sleep(1)
        print("The regions this Pokedex support are:")
        sleep(1)
        print(", ".join(self.regionsdata.keys()))
        sleep(1)
        print("Which region would you like to explore?")
        self.rundex()
    
    def displayhelp(self):
        """
        Displays a list of the available commands.
        """
        print("Valid commands are: \"<region>\" \"regions\" \"<pokemon>\" \"pokemon\" \"<data>\" \"data\" \"back\" \"help\" \"quit\"")
        sleep(1)
    
    def displayregions(self):
        """
        Displays the regions available.
        """
        print("The regions this Pokedex support are:")
        sleep(1)
        print(", ".join(self.regionsdata.keys()))
        sleep(1)
    
    def displaypokemon(self, region:str):
        """
        Displays the pokemon available.
        """
        print(f"The Pokemon currently in this region are:")
        sleep(1)
        print(", ".join(self.regionsdata[region].keys()))
        sleep(1)
    
    def displaydata(self):
        """
        Displays the data available.
        """
        print(f"The current data available for {self.currentpokemon} is:")
        sleep(1)
        print(", ".join(self.pokemondata.keys()))
        sleep(1)
    
    def enterregion(self, userinput):
        """
        Executed when the user enters the region level of the program.
        """
        self.regiondir(userinput)
        print(f"Now entering the {userinput.title()} region!")
        sleep(1)
        print(f"The Pokemon currently in this region are:")
        sleep(1)
        print(", ".join(self.regionsdata[userinput].keys()))
        sleep(1)
        print("Which Pokemon would you like to know more about?")
    
    def enterpokemondata(self, userinput):
        """
        Executed when the user enters the pokemondata level of the program.
        """
        self.pokemondir(self.currentregion, userinput)
        self.pokemondata = self.accesspokemondata(self.currentregion, self.currentpokemon)
        print(f"Getting data for {userinput}...")
        sleep(2)
        print(f"The current data available for {self.currentpokemon} is:")
        print(", ".join(self.pokemondata.keys()))
        sleep(1)
        print(f"What would you like to know about {self.currentpokemon}?")
    
    def rundex(self):
        """
        runs the Pokedex
        """
        # Everything below this while True loop is contained within the / (home) directory
        while True:
            userinput = input("").lower().strip()
            
            if userinput == "back":
                print("That command cannot be executed at this time!")
                sleep(1)
            
            elif userinput == "quit":
                exit()
            
            elif userinput == "help":
                self.displayhelp()
            
            elif userinput == "regions":
                self.displayregions()
            
            elif userinput == "pokemon":
                print("Please enter a region first!")
                sleep(1)
            
            elif userinput == "data":
                print("Please enter a region first!")
                sleep(1)
            
            elif userinput in self.regionsdata:
                self.enterregion(userinput)


                # Everything below this while True loop is contained within the /<region> directory
                while True:
                    userinput = input("").lower().strip()
                    
                    if userinput == "back":
                        self.currentregion = None
                        break
                    
                    elif userinput == "quit":
                        exit()
                    
                    elif userinput == "help":
                        self.displayhelp()
                    
                    elif userinput == "regions":
                        self.displayregions()
                    
                    elif userinput == "pokemon":
                        self.displaypokemon(self.currentregion)
                    
                    elif userinput == "data":
                        print("Please select a Pokemon first!")
                        sleep(1)
                    
                    elif self.currentregion and userinput in self.regionsdata[self.currentregion]:
                        self.enterpokemondata(userinput)


                        # Everything below this while True loop is contained within the /<region>/<pokemon> directory
                        while True:
                            userinput = input("").lower().strip()
                            
                            if userinput == "back":
                                self.currentpokemon = None
                                break
                            
                            elif userinput == "quit":
                                exit()
                            
                            elif userinput == "help":
                                self.displayhelp()
                            
                            elif userinput == "regions":
                                self.displayregions()
                            
                            elif userinput == "pokemon":
                                self.displaypokemon(self.currentregion)
                            
                            elif userinput == "data":
                                self.displaydata()
                            
                            elif userinput == "name" and self.currentregion and self.currentpokemon and userinput in self.pokemondata:
                                print("Fetching name...")
                                sleep(1)
                                print(f"{self.currentpokemon}'s name is {self.accessname(self.currentregion, self.currentpokemon)}")
                                sleep(1)
                            
                            elif userinput == "type" and self.currentregion and self.currentpokemon and userinput in self.pokemondata:
                                print("Fetching type...")
                                sleep(1)
                                print(f"{self.currentpokemon}'s type is {self.accesstype(self.currentregion, self.currentpokemon)}")
                                sleep(1)
                            
                            elif userinput == "weakness" and self.currentregion and self.currentpokemon and userinput in self.pokemondata:
                                print("Fetching weakness...")
                                sleep(1)
                                print(f"{self.currentpokemon}'s weakness is {self.accessweakness(self.currentregion, self.currentpokemon)}")
                                sleep(1)
                            
                            elif userinput == "evolves" and self.currentregion and self.currentpokemon and userinput in self.pokemondata:
                                print("Fetching evolution level...")
                                sleep(1)
                                print(f"{self.currentpokemon} evolves at level {self.accessevolves(self.currentregion, self.currentpokemon)}")
                                sleep(1)
                            
                            elif userinput == "description" and self.currentregion and self.currentpokemon and userinput in self.pokemondata:
                                print("Fetching description...")
                                sleep(1)
                                print(self.accessdescription(self.currentregion, self.currentpokemon))
                                sleep(1)


                            else:
                                print("The Pokedex does not contain that data!")
                            
                            print(f"What would you like to know about {self.currentpokemon}?")


                    else:
                        print("That Pokemon is not in this Pokedex/region!")
                        sleep(1)

                    print("Which Pokemon would you like to know more about?")


            print("Which region would you like to explore?")



if __name__ == "__main__":
    p = Pokedex()
    p.startdex()