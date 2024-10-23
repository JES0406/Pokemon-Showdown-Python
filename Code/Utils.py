import re
import random

def normalize_name(name: str) -> str:
    # Use a regular expression to remove unwanted characters
    return re.sub(r'[ \-\'.’%:]', '', name.lower())

def get_choice(options: list, weights: list = None, n = 1) -> str:
        """
        Get a random choice from a dictionary.
        :param data: Dictionary containing the choices.
        :param n: Number of choices to be returned.
        :return: Random choice(s).
        """
        return random.choices(options, weights=weights, k=n) # Return a list of n choices