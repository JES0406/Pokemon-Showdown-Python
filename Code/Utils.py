import re
import random

def normalize_name(name: str) -> str:
    # Use a regular expression to remove unwanted characters
    return re.sub(r'[ \-\'.’%:]', '', name.lower())

def get_choice(data: dict, n: int = 1):
        """
        Get a random choice from a dictionary.
        :param data: Dictionary containing the choices.
        :param n: Number of choices to be returned.
        :return: Random choice(s).
        """
        options = list(data.keys())
        weights = list(data.values())
        return random.choices(options, weights=weights, k=n) # Return a list of n choices