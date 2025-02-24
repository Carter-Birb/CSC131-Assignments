from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"success": True, "me": "Carter"})

@app.route("/pikachu", methods=["GET"])
def pikachu():
    entry = {
        "type": "electric",
        "weakness": "ground",
        "region": "kanto",
        "description": "This pokemon has electricity-storing pouches on its cheeks. These appear to become electrically charged during the night while pikachu sleeps. It occasionally discharges electricity when it is dozy after waking up. It has small electric sacs on both its cheeks.",
    }
    data = jsonify(entry)
    return data

@app.route("/lucario", methods=["GET"])
def lucario():
    entry = {
        "type": "fighting/steel",
        "weakness": "fighting, ground, fire",
        "region": "sinnoh",
        "description": "Lucario reads its opponent's feelings with its aura waves. It finds out things it would rather not know, so it gets stressed out easily. It controls waves known as auras, which are powerful enough to pulverize huge rocks. It uses these waves to take down its prey.",
    }
    data = jsonify(entry)
    return data

@app.route("/rayquaza", methods=["GET"])
def rayquaza():
    entry = {
        "type": "flying/dragon",
        "weakness": "fairy, rock, ice, dragon",
        "region": "hoenn",
        "description": "Rayquaza is said to have lived for hundreds of millions of years. Legends remain of how it put to rest the clash between Kyogre and Groudon. It flies forever through the ozone layer, consuming meteoroids for sustenance. The many meteoroids in its body provide the energy it needs to Mega Evolve.",
    }
    data = jsonify(entry)
    return data

@app.route("/ceruledge", methods=["GET"])
def ceruledge():
    entry = {
        "type": "ghost/fire",
        "weakness": "water, ground, rock",
        "region": "paldea",
        "description": "Ceruledge dons an old set of armor steeped in grudges and wields blades made of fire and ghost energy. In battle, these blades transform into great swords to increase Ceruledge’s power. Cuts from these great swords leave wounds from which life energy will flow.",
    }
    data = jsonify(entry)
    return data

@app.route("/charizard", methods=["GET"])
def charizard():
    entry = {
        "type": "fire/flying",
        "weakness": "water, rock, electric",
        "region": "kanto",
        "description": "It boasts speed and maneuverability greater than that of a jet fighter. The flame inside its body burns hotter than 3,600 degrees Fahrenheit. When Charizard roars, that temperature climbs even higher. This colossal, flame-winged figure of a Charizard was brought about by Gigantamax energy.",
    }
    data = jsonify(entry)
    return data