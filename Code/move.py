'''
Module containing the class Move.

A move has a name, type, category, power, accuracy, pp, priority, target, effect and other relevant information.
'''

class Move:
    def __init__(self, name: str, type: str, category: str, power: int, accuracy: int, pp: int, priority: int, target: str, effect: str):
        self._name = name
        self._type = type
        self._category = category
        self._base_power = power
        self._power = power
        self._accuracy = accuracy
        self._base_pp = pp
        self._pp = pp
        self._priority = priority
        self._target = target
        self._effect = effect

    # Setters and getters
    @property
    def name(self):
        return self._name
    
    @property
    def type(self):
        return self._type
    
    @property
    def category(self):
        return self._category
    
    @property
    def power(self):
        return self._power
    
    @power.setter
    def power(self, power):
        self._power = power

    @property
    def accuracy(self):
        return self._accuracy
    
    @accuracy.setter
    def accuracy(self, accuracy):
        if accuracy > 100:
            self._accuracy = 100

    @property
    def pp(self):
        return self._pp
    
    @pp.setter
    def pp(self, pp):
        if pp > self._base_pp:
            self._pp = self._base_pp

    @property
    def priority(self):
        return self._priority
    
    @property
    def target(self):
        return self._target
    
    @property
    def effect(self):
        return self._effect
    
    # Methods
    def use(self):
        self._pp -= 1
        return self._power
    
    def __str__(self):
        return f'''
        Name: {self._name}
        Type: {self._type}
        Category: {self._category}
        Power: {self._power if self.power == self._base_power else f'{self._power} (base: {self._base_power})'}
        Accuracy: {self._accuracy}
        PP: {self._pp}/{self._base_pp}
        Priority: {self._priority}
        Target: {self._target}
        Effect: {self._effect}
        '''