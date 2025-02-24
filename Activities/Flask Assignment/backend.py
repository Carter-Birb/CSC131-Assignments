##########################################
# Carter Landry
# 2/24/25
# This is a Flask Project that uses pokedex entries as endpoints.
##########################################


from flask import Flask, jsonify, request

app = Flask(__name__)
# As a little project, I may host a github repository to allow friends to add dex entries

"""
DEXENTRIES are of the form:

pokemon name (lower): {
    "name": "pokemon name",
    "type": "pokemon type(s)",
    "weakness": "pokemon weakness(es)",
    "region": "pokemon region",
    "description": "pokemon pokedex description/entry",
    }
"""

DEXENTRIES = {
    "pikachu": {
        "name": "pikachu",
        "type": "electric",
        "weakness": "ground",
        "region": "kanto",
        "description": "This pokemon has electricity-storing pouches on its cheeks. These appear to become electrically charged during the night while pikachu sleeps. It occasionally discharges electricity when it is dozy after waking up. It has small electric sacs on both its cheeks.",
    },
    "lucario": {
        "name": "lucario",
        "type": "fighting/steel",
        "weakness": "fighting, ground, fire",
        "region": "sinnoh",
        "description": "Lucario reads its opponent's feelings with its aura waves. It finds out things it would rather not know, so it gets stressed out easily. It controls waves known as auras, which are powerful enough to pulverize huge rocks. It uses these waves to take down its prey.",
    },
    "rayquaza": {
        "name": "rayquaza",
        "type": "flying/dragon",
        "weakness": "fairy, rock, ice, dragon",
        "region": "hoenn",
        "description": "Rayquaza is said to have lived for hundreds of millions of years. Legends remain of how it put to rest the clash between Kyogre and Groudon. It flies forever through the ozone layer, consuming meteoroids for sustenance. The many meteoroids in its body provide the energy it needs to Mega Evolve.",
    },
    "ceruledge": {
        "name": "ceruledge",
        "type": "ghost/fire",
        "weakness": "water, ground, rock",
        "region": "paldea",
        "description": "Ceruledge dons an old set of armor steeped in grudges and wields blades made of fire and ghost energy. In battle, these blades transform into great swords to increase Ceruledge’s power. Cuts from these great swords leave wounds from which life energy will flow.",
    },
    "charizard": {
        "name": "charizard",
        "type": "fire/flying",
        "weakness": "water, rock, electric",
        "region": "kanto",
        "description": "It boasts speed and maneuverability greater than that of a jet fighter. The flame inside its body burns hotter than 3,600 degrees Fahrenheit. When Charizard roars, that temperature climbs even higher. This colossal, flame-winged figure of a Charizard was brought about by Gigantamax energy.",
    },
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"success": True, "me": "Carter"})


# Returns the pokemon within the pokedex when the program is run. This updates dynamically with pokemon added.
@app.route("/pokedexlist", methods=["GET"])
def pokedexlist():
    """
    returns the pokemon currently in the pokedex (keys)
    """
    return jsonify(list(DEXENTRIES.keys()))


# This creates a dynamic endpoint system that will update with pokemon added to the DEXENTRIES dictionary.
@app.route("/<pokemon>", methods=["GET"])
def getpokemon(pokemon:str):
    """
    returns the information from a given pokemon
    """
    if pokemon in DEXENTRIES:
        return jsonify(DEXENTRIES[pokemon])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8000")