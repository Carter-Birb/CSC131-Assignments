# As a little project, I may host a github repository to allow friends to add dex entries

"""
DEXENTRIES are of the form:

region: {
    pokemon name: {
        "name": "Name",
        "type": "Type",
        "weakness": "Weakness(s)",
        "evolves" : lvl the pokemon evolves at (int)
        "description": "Pokedex description of Pokemon"
    }
}
"""

DEXENTRIES = {
    "kanto": {
        "bulbasaur": {
            "name": "Bulbasaur",
            "type": "grass/poison",
            "weakness": "fire/psychic/flying/ice",
            "evolves": 16,
            "description": "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon."
        },
        "charmander": {
            "name": "Charmander",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 16,
            "description": "Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail."
        },
        "squirtle": {
            "name": "Squirtle",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 16,
            "description": "After birth, its back swells and hardens into a shell. It powerfully sprays foam from its mouth."
        }
    },
    
    "johto": {
        "chikorita": {
            "name": "Chikorita",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 16,
            "description": "A sweet aroma gently wafts from the leaf on its head. It is docile and loves to soak up the sun's rays."
        },
        "cyndaquil": {
            "name": "Cyndaquil",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 14,
            "description": "It usually stays hunched over. If it is angry or surprised, it shoots flames out of its back."
        },
        "totodile": {
            "name": "Totodile",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 18,
            "description": "It is small but rough and tough. It won't hesitate to take a bite out of anything that moves."
        }
    },
    
    "hoenn": {
        "treecko": {
            "name": "Treecko",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 16,
            "description": "It quickly scales even vertical walls. It senses humidity with its tail to predict the next day's weather."
        },
        "torchic": {
            "name": "Torchic",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 16,
            "description": "Inside its body is a place where it keeps its flame. Give it a hug—it will be glowing with warmth."
        },
        "mudkip": {
            "name": "Mudkip",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 16,
            "description": "To alert it, the fin on its head senses the flow of water. It has the strength to hurl boulders."
        }
    },
    
    "sinnoh": {
        "turtwig": {
            "name": "Turtwig",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 18,
            "description": "It undertakes photosynthesis with its body, making oxygen. The leaf on its head wilts if it is thirsty."
        },
        "chimchar": {
            "name": "Chimchar",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 14,
            "description": "Its fiery rear end is fueled by gas made in its belly. Even rain can’t extinguish the fire."
        },
        "piplup": {
            "name": "Piplup",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 16,
            "description": "Because it is very proud, it hates accepting food from people. Its thick down guards it from cold."
        }
    },
    
    "unova": {
        "snivy": {
            "name": "Snivy",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 17,
            "description": "It is very intelligent and calm. Being exposed to lots of sunlight makes its movements swifter."
        },
        "tepig": {
            "name": "Tepig",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 17,
            "description": "It blows fire through its nose. When it catches a cold, the fire blazes weaker than usual."
        },
        "oshawott": {
            "name": "Oshawott",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 17,
            "description": "The scalchop on its stomach isn’t just used for battle—it can be used to break open hard berries."
        }
    },
    
    "kalos": {
        "chespin": {
            "name": "Chespin",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 16,
            "description": "It relies on its shell for protection. It stays on guard and keeps a watchful eye on its surroundings."
        },
        "fennekin": {
            "name": "Fennekin",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 16,
            "description": "Eating a twig fills it with energy, and its roomy ears give vent to air hotter than 390 degrees Fahrenheit."
        },
        "froakie": {
            "name": "Froakie",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 16,
            "description": "It protects its skin by covering itself with tiny bubbles."
        }
    },
    
    "alola": {
        "rowlet": {
            "name": "Rowlet",
            "type": "grass/flying",
            "weakness": "fire/ice/flying/poison/rock",
            "evolves": 17,
            "description": "Silently it glides, drawing near its target. Before they even notice it, it begins to pelt them with vicious kicks."
        },
        "litten": {
            "name": "Litten",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 17,
            "description": "While grooming itself, it builds up fur inside its stomach. It sets the fur alight and spews fiery attacks."
        },
        "popplio": {
            "name": "Popplio",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 17,
            "description": "Popplio's swimming speed is known to exceed 25 mph. It takes pride in its acrobatic abilities."
        }
    },
    
    "galar": {
        "grookey": {
            "name": "Grookey",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 16,
            "description": "It attacks with rapid beats of its stick. As it strikes with amazing speed, it gets more and more pumped."
        },
        "scorbunny": {
            "name": "Scorbunny",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 16,
            "description": "A warm-up of running around gets fire energy coursing through this Pokémon’s body."
        },
        "sobble": {
            "name": "Sobble",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 16,
            "description": "When it gets wet, its skin changes color, and this Pokémon becomes invisible as if it were camouflaged."
        }
    },
    
    "paldea": {
        "sprigatito": {
            "name": "Sprigatito",
            "type": "grass",
            "weakness": "fire/ice/poison/flying/bug",
            "evolves": 16,
            "description": "Its fluffy fur is similar in composition to plants. This Pokémon frequently washes its face to keep it from drying out."
        },
        "fuecoco": {
            "name": "Fuecoco",
            "type": "fire",
            "weakness": "water/rock/ground",
            "evolves": 16,
            "description": "It lies on warm rocks and uses the heat absorbed by its square scales to create fire energy."
        },
        "quaxly": {
            "name": "Quaxly",
            "type": "water",
            "weakness": "electric/grass",
            "evolves": 16,
            "description": "Its glossy body is always polished, and it dislikes getting dirty."
        }
    },
    
    
}
