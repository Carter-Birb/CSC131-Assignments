##########################################
# Carter Landry
# 2/24/25
# This is a Flask Project that uses pokedex entries as endpoints.
##########################################


from flask import Flask, jsonify, request
from pokedexentries import DEXENTRIES

app = Flask(__name__)

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