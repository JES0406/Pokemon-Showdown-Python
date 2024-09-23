from Code.DataStructures.Battle import Battle
from Code.Constructors.BaseConstructor import BaseConstructor
from Code.Constructors.PlayerConstructor import PlayerConstructor

class BattleConstructor(BaseConstructor):
    def __init__(self):
        super().__init__()
        self.player_constructor = PlayerConstructor()
        
    def create(self, battle_data: dict):
        battle = Battle()
        for player_data in battle_data['players']:
            player = self.player_constructor.create(player_data)
            battle.add_player(player)
        return battle