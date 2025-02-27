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

# The following entries were added by ChatGPT: #
# Adding more Pokémon to Kanto
DEXENTRIES["kanto"].update({
    "pikachu": {
        "name": "Pikachu",
        "type": "electric",
        "weakness": "ground",
        "evolves": 0,
        "description": "Pikachu stores electricity in its cheeks and releases it when threatened."
    },
    "eevee": {
        "name": "Eevee",
        "type": "normal",
        "weakness": "fighting",
        "evolves": 0,
        "description": "Its unstable genetic makeup allows it to evolve into various forms."
    }
})

# Adding more Pokémon to Johto
DEXENTRIES["johto"].update({
    "mareep": {
        "name": "Mareep",
        "type": "electric",
        "weakness": "ground",
        "evolves": 15,
        "description": "Its fluffy fleece grows continuously. In the summer, the fleece is fully shed, but it grows back in a week."
    },
    "houndour": {
        "name": "Houndour",
        "type": "dark/fire",
        "weakness": "water/rock/fighting/ground",
        "evolves": 24,
        "description": "Houndour communicate with each other using a variety of cries to corner prey."
    }
})

# Adding more Pokémon to Hoenn
DEXENTRIES["hoenn"].update({
    "ralts": {
        "name": "Ralts",
        "type": "psychic/fairy",
        "weakness": "ghost/poison/steel",
        "evolves": 20,
        "description": "If its trainer is in a cheerful mood, this Pokémon grows cheerful and joyful in the same way."
    },
    "aron": {
        "name": "Aron",
        "type": "steel/rock",
        "weakness": "fighting/ground/water",
        "evolves": 32,
        "description": "Aron has a body of steel. It eats iron ore—occasionally causing tunnel collapses in mountain mines."
    }
})

# Adding more Pokémon to Sinnoh
DEXENTRIES["sinnoh"].update({
    "riolu": {
        "name": "Riolu",
        "type": "fighting",
        "weakness": "flying/psychic/fairy",
        "evolves": 25,
        "description": "It has the power to see emotions like joy and rage in the form of waves."
    },
    "shinx": {
        "name": "Shinx",
        "type": "electric",
        "weakness": "ground",
        "evolves": 15,
        "description": "The extension and contraction of its muscles generates electricity. It glows when in trouble."
    }
})

# Adding more Pokémon to Unova
DEXENTRIES["unova"].update({
    "zorua": {
        "name": "Zorua",
        "type": "dark",
        "weakness": "bug/fighting/fairy",
        "evolves": 30,
        "description": "Zorua often transforms into other Pokémon to escape danger or trick opponents."
    },
    "axew": {
        "name": "Axew",
        "type": "dragon",
        "weakness": "ice/dragon/fairy",
        "evolves": 38,
        "description": "Axew's tusks can regenerate if broken, and they grow stronger each time they regrow."
    }
})

# Adding more Pokémon to Kalos
DEXENTRIES["kalos"].update({
    "helioptile": {
        "name": "Helioptile",
        "type": "electric/normal",
        "weakness": "fighting/ground",
        "evolves": 25,
        "description": "They make their home in deserts. They can generate electricity from sunlight, allowing them to store energy."
    },
    "noibat": {
        "name": "Noibat",
        "type": "flying/dragon",
        "weakness": "rock/ice/dragon/fairy",
        "evolves": 48,
        "description": "It emits ultrasonic waves as it flies. These waves can damage and stun opponents."
    }
})

# Adding more Pokémon to Alola
DEXENTRIES["alola"].update({
    "rockruff": {
        "name": "Rockruff",
        "type": "rock",
        "weakness": "water/grass/steel/fighting/ground",
        "evolves": 25,
        "description": "Rockruff has an excellent sense of smell. Once it has smelled something, it never forgets the scent."
    },
    "stufful": {
        "name": "Stufful",
        "type": "normal/fighting",
        "weakness": "fighting/flying/psychic/fairy",
        "evolves": 27,
        "description": "Stufful dislikes being hugged, despite its cute appearance. It has powerful strength hidden in its small body."
    }
})

# Adding more Pokémon to Galar
DEXENTRIES["galar"].update({
    "yamper": {
        "name": "Yamper",
        "type": "electric",
        "weakness": "ground",
        "evolves": 25,
        "description": "Yamper loves to chase after things that move fast, like people on bicycles."
    },
    "rolycoly": {
        "name": "Rolycoly",
        "type": "rock",
        "weakness": "water/grass/steel/fighting/ground",
        "evolves": 18,
        "description": "Rolycoly can travel smoothly over the roughest terrain. It uses the coal in its body as a source of energy."
    }
})

# Adding more Pokémon to Paldea
DEXENTRIES["paldea"].update({
    "fidough": {
        "name": "Fidough",
        "type": "fairy",
        "weakness": "poison/steel",
        "evolves": 26,
        "description": "Its breath contains yeast. It ferments things within a short time span."
    },
    "tinkatink": {
        "name": "Tinkatink",
        "type": "fairy/steel",
        "weakness": "fire/ground",
        "evolves": 24,
        "description": "Tinkatink collects discarded metal to craft its own hammer, which it uses to protect itself."
    }
})