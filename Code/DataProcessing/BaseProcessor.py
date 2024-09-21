class BaseProcessor:
    def __init__(self, data=None):
        """
        Initialize the processor
        """
        self.data = data

    def validate_data(self):
        """
        Validate the input data to ensure it's in the correct format.
        :return: True if the data is valid, otherwise False.
        """
        if not isinstance(self.data, dict):
            print("Invalid data type. Expected dictionary.")
            return False
        return True

    def process(self):
        """
        Process the data. This method is meant to be overridden by subclasses
        to handle specific data transformations.
        """
        raise NotImplementedError("Subclasses should implement this method")
    
    def get_needed():
        """
        Get the needed keys. This method is meant to be overridden by subclasses
        to handle specific data retrieval.
        """
        raise NotImplementedError("Subclasses should implement this method")
    
    def get_data():
        """
        Get the data. This method is meant to be overridden by subclasses
        to handle specific data retrieval.
        """
        raise NotImplementedError("Subclasses should implement this method")

    def load_data(self, filepath):
        """
        Load data from a file, which could be used for initializing the processor.
        :param filepath: Path to the data file (JSON, CSV, etc.)
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                import json
                data = json.load(file)
        except FileNotFoundError:
            print(f"File {filepath} not found.")
        except Exception as e:
            print(f"Error loading file: {e}")
        return data

    def save_data(self, filepath):
        """
        Save the processed data to a file (e.g., JSON format).
        :param filepath: Path to the output file.
        """
        try:
            with open(filepath, 'w') as file:
                import json
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def print_data(self):
        """
        Utility method to print the data (for debugging or review purposes).
        """
        print(self.data)
