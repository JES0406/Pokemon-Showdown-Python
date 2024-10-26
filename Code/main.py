"""
The main program
Right now it only makes a battle
"""

from Code.Constructors.BattleConstructor import BattleConstructor
import subprocess
import os, sys

if __name__ == "__main__":
    import os

    file_paths = file_paths = ['Datasets/Moves.json', 'Datasets/Movesets.json', 'Datasets/Pokemon.json']

    for file_path in file_paths:
        if not os.path.exists(file_path):
            subprocess.run(['python', 'Code/DataProcessing/ProcessData.py'])
            break
    else:
        print("All good")
    constructor = BattleConstructor()
    battle = constructor.create(
        battle_data= {
            "players":
            [
                {
                    "name" : input("Insert your name: "),
                    "team": [int(input("How many pokemon do you want (There is no protection, dont be a jackass): "))]
                },
                {
                    "name" : input("Insert your name: "),
                    "team": [int(input("How many pokemon do you want (There is no protection, dont be a jackass): "))]
                }
            ]
        }
    )
    battle.run()