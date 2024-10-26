import re
import random
import numpy as np

def normalize_name(name: str) -> str:
    # Use a regular expression to remove unwanted characters
    return re.sub(r'[ \-\'.’%:]', '', name.lower())

def get_choice(options: list, weights: list = None, n=1) -> list:
    """
    Get a random choice from a list of options with optional weights, ensuring unique choices.
    :param options: List of available options.
    :param weights: List of weights corresponding to each option.
    :param n: Number of unique choices to be returned.
    :return: List of unique random choices.
    """
    if len(options) != len(weights):
        raise ValueError("The number of options must be equal to the amount of weights")
        
    if round(sum(weights),0) != n: # We round because of float point operations
        raise ValueError("The weights are wrong")
        
    
    avaliable_options = options.copy()
    avaliable_weights = weights.copy()
    selected = []
    k = 0
    for i in range(len(weights)):
        if weights[i] == 1 and k < n:
            option = options[i]
            selected.append(option)
            avaliable_options.remove(option)
            avaliable_weights.remove(weights[i])
            k += 1
    if k < n:
        avaliable_weights = normalize_weights(avaliable_weights, n-k)
        choices = np.random.choice(avaliable_options, p = avaliable_weights, size=n-k, replace = False)
        for choice in choices:
            selected.append(choice)
    return selected

def normalize_weights(weights, n):
    new_weights = [i/n for i in weights]
    new_weights[-1] += 1 - sum(new_weights)
    return new_weights