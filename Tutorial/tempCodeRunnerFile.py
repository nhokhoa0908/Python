# Define the player and the Pokémon
player = {
    "name": "Ash",
    "level": 5,
    "pokémon": [
        { "name": "Pikachu", "type": "electric", "level": 7 },
        { "name": "Charmander", "type": "fire", "level": 5 },
    ],
}

enemy_pokemon = { "name": "Bulbasaur", "type": "grass", "level": 6 }

# Define the battle function
def battle():
    print(
        f"{player['name']} has challenged {enemy_pokemon['name']} to a battle!"
    )

    # Determine the stronger Pokémon
    player_pokemon = player["pokémon"][0] if player["pokémon"][0]["level"] > player["pokémon"][1]["level"] else player["pokémon"][1]

    print(f"{player['name']} sends out {player_pokemon['name']}!")
    print(f"{enemy_pokemon['name']} appears!")

    # Check who wins the battle
    if player_pokemon["level"] > enemy_pokemon["level"]:
        print(f"{player_pokemon['name']} wins the battle!")
    else:
        print(f"{enemy_pokemon['name']} wins the battle!")

# Call the battle function
battle()