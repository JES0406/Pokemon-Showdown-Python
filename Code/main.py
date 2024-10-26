"""
The main program
Right now it only makes a battle
"""

from Code.Constructors.BattleConstructor import BattleConstructor

if __name__ == "__main__":
    constructor = BattleConstructor()
    constructor.create(
        battle_data= {
            "players":
            [
                {
                    "name" : input("Insert your name"),
                    "team": int(input("How many pokemon do you want (There is no protection, dont be a jackass)"))
                },
                {
                    "name" : input("Insert your name"),
                    "team": int(input("How many pokemon do you want (There is no protection, dont be a jackass)"))
                }
            ]
        }
    )