'''
Module for the BaseConstructor class.

Creates a BaseConstructor, which is the base class for all constructors.
The BaseConstructor class contains methods that, in the majority of cases, are used or overwritten by the child classes.
'''

import json
import random

class BaseConstructor:
    def __init__(self):
        self._data = None
        self._structure = None

    def load_data(self, path: str) -> dict:
        """
        Load data from a file.
        :param path: Path to the file containing the data.
        :return: Dictionary containing the data.
        """
        return json.load(open(path, 'r'))
    
    def create(self, data: dict):
        """
        Create the data structure.
        This method should be overwritten by the child classes.
        :param data: Data to be processed.
        """
        raise NotImplementedError("Subclasses should implement this method")
    
    def get_structure(self):
        """
        Return the data structure.
        :return: Data structure.
        """
        return self._structure