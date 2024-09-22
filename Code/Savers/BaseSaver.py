import csv
class BaseSaver:
    def __init__(self):
        pass

    def save(self, data, save_path: str):
        '''Save the data to a csv file'''
        if not self.check_if_exists(data, save_path):
            with open(save_path, 'a') as file:
                file.write(repr(data) + '\n')
        return True
    
    def check_if_exists(self, data, save_path: str):
        '''Check if the data is already saved'''
        with open(save_path, 'r') as file:
            for i, line in enumerate(file):
                if repr(data) in line:
                    return i
        return False
    
    def modify_csv(self, data: str, save_path: str, index: int):
        '''Modify the csv file'''
        with open(save_path, 'r') as file:
            reader = csv.reader(file)
            lines = list(reader)

        if index >= len(lines):
            raise IndexError('Index out of range')
        else:
            lines[index] = repr(data) + '\n'

        with open(save_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(lines)