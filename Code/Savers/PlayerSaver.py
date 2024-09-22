import csv
from Code.Savers.BaseSaver import BaseSaver
from Code.DataStructures.Player import Player

class PlayerSaver(BaseSaver):
    def __init__(self):
        super().__init__()

    def save(self, player: Player, save_path: str, result: str = None):
        '''Save the player data to a csv file'''
        index = self.check_if_exists(player, save_path)
        if index == False:
            with open(save_path, 'a') as file:
                file.write(repr(player) + ',[0,0]' + '\n')
        else:
            self.update_record(player, save_path, result, index)

    def get_record(self, save_path: str, index: int) -> str:
        '''Get the record of the player in the csv file'''
        with open(save_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            record = rows[index][2]
            return record
            
        return None
    
    def update_record(self, player: Player, save_path: str, result: int, index: int):
        '''Update the record of the player in the csv file
        The record is updated with the result of the match
        The resut is 0 if the player lost and 1 if the player won'''
        record = self.get_record(save_path, index)
        record = record[1:-1].split(',')

        record[1-result] = str(int(record[0]) + 1)
        data = repr(player) + ',' + str(record) + '\n'
        self.modify_csv(data, save_path, index)
