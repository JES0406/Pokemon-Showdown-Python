# Pokemon Showdown Clone in Python

## Description
A Python-based version of the smogon web game Pokemon Showdown, a popular pokemon battle simulator. This project is a work in progress and is being developed as a learning experience.
The project will include features like a random team creator, a battle simulator, local and online multiplayer, a database of pokemon and moves, and a ranking system, sustiained by a database of saved games and results.

## Goals
- Create a fully functional turn-based battle system with Pokémon stats, abilities, and moves.
- Implement player vs AI battles and later player vs player (PvP) functionality.
- Eventually expand to multiplayer battles using Python networking libraries.

## Features
- [x] Plain text simulator.
- [x] Random team generator.
- [ ] Local multiplayer.
- [ ] Online multiplayer.
- [ ] Ranking system.
- [x] Database of pokemon and moves.
- [ ] Database of saved games and results.

## Technologies
- Python 3.12
- Pygame (to be implemented)
- SQLite3 (to be implemented)
- Socket (to be implemented)
- Unit testing (to be implemented)

## Getting Started
1. Clone the repository.
```bash
git clone https://github.com/JES0406/Pokemon-Showdown-Python.git
cd Pokemon-Showdown-Python
```
2. Install the required packages.
```bash
pip install -r requirements.txt
```
3. Run the main file.
```bash
python main.py
```

## How to Play
- Select the game mode you want to play.
  - Select if single player or multiplayer.
- Select the Pokémon you want to use.
- Each player takes turns selecting a move.
- The game ends when all the Pokémon of one player are defeated.

## LICENSE
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Screenshots (coming soon)
Once the project is more developed, screenshots will be added to the README.

## Design decisions
- **Csv for data storage**: For simplicity in the initial stages, the data of the Pokémon and moves will be stored in CSV files. 
- **Object-oriented design**: The project will be designed using object-oriented programming principles to make the code more modular and easier to maintain.
- **Separation of concerns**: The project will be divided into different modules to separate the game logic from the user interface and the data storage.
- **Damage rounding**: The damage calculation will be rounded to the nearest integer at the end of the calculation in order to make it easier to understand and implement.
- **Pokemons available**: Using the dataset of competitive Pokémon, the project will have a list of Pokémon available to use in the game. We will prioritize the latests generations of Pokémon for building the teams.
- **Movesets file**: The movesets are in a json file because not all pokemon have the same attributes. The movesets are stored in a json file to make it easier to access the data.

## Acknowledgements
- The original idea of the project was inspired by the Pokémon Showdown from smogon. The main website can be found [here](https://pokemonshowdown.com/). This project is not affiliated with Pokémon Showdown or smogon.
- Datasets of move-data and pokemon-data taken from: https://www.kaggle.com/datasets/n2cholas/competitive-pokemon-dataset?resource=download
- Dataset of moveset from: https://github.com/pkmn/randbats/blob/main/data/
- The project has been supported by ChatGPT and GitHub Copilot.
```
