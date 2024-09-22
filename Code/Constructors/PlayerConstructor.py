
from Code.DataStructures.Player import Player
from Code.Constructors.BaseConstructor import BaseConstructor
from Code.Constructors.TeamConstructor import TeamConstructor
import csv


class PlayerConstructor(BaseConstructor):
    def __init__(self):
        super().__init__()
        self.team_constructor = TeamConstructor()

    def create(self, player_data: dict):
        # We open the logs file to see if the player has already has an id

        id_ = self.get_id(player_data, 'Logs/Players.csv')
        team = self.team_constructor.create(player_data['team'])
        player = Player(player_data['name'], team, id_)
        return player
    
    def get_id(self, player_data: dict, player_log_path: str):
        try:
            with open(player_log_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] == player_data['name']:
                        id_ = row[0]
                        break
                else:
                    id_ = reader.line_num
            return id_
                    
        except FileNotFoundError:
            raise FileNotFoundError('Player log file not found')