'''
Module containing the class Move.

A move has a name, type, category, power, accuracy, pp, priority, target, effect and other relevant information.
'''

class Move:
    def __init__(self, 
                 num: int = None, 
                 name: str = None, 
                 type_: str = None, 
                 category: str = None, 
                 pp: int = None, 
                 basePower: int = None, 
                 accuracy: int = None, 
                 priority: int = None, 
                 flags: dict = None, 
                 secondary: dict = None, 
                 target: str = None, 
                 zMove: dict = None, 
                 maxMove: dict = None, 
                 recoil: dict = None, 
                 heal: dict = None, 
                 critRatio: int = None, 
                 drain: dict = None, 
                 forceSwitch: bool = None, 
                 selfBoost: dict = None, 
                 weather: str = None, 
                 additionalEffects: dict = None):
        """
        Initialize the Move class with attributes from the moves JSON.
        All attributes are private, and access is controlled through @property decorators.
        """
        self._num = num
        self._name = name

        self._type = type_
        self._category = category
        self._base_pp = pp
        self._pp = pp
        self._basePower = basePower
        self._power = basePower
        self._accuracy = accuracy
        self._priority = priority
        self._target = target

        self._flags = flags if flags is not None else {}
        self._secondary = secondary
        self._zMove = zMove
        self._maxMove = maxMove
        self._recoil = recoil
        self._heal = heal
        self._critRatio = critRatio
        self._drain = drain
        self._forceSwitch = forceSwitch
        self._selfBoost = selfBoost
        self._weather = weather
        self._additionalEffects = additionalEffects if additionalEffects is not None else {}

    # Setters and getters
    @property
    def num(self):
        return self._num

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
    def basePP(self):
        return self._base_pp
    
    @property
    def pp(self):
        return self._pp
    
    @pp.setter
    def pp(self, pp):
        if pp > self._base_pp:
            self._pp = self._base_pp
        else:
            self._pp = pp

    @property
    def basePower(self):
        return self._basePower
    
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
        else:
            self._accuracy = accuracy

    @property
    def priority(self):
        return self._priority
    
    @priority.setter
    def priority(self, priority):
        if abs(priority) > 4:
            self._priority = 4 if priority > 0 else -4
        else:
            self._priority = priority
    
    @property
    def target(self):
        return self._target
    
    @property
    def flags(self):
        return self._flags
    
    @property
    def secondary(self):
        return self._secondary
    
    @property
    def zMove(self):
        return self._zMove
    
    @property
    def maxMove(self):
        return self._maxMove
    
    @property
    def recoil(self):
        return self._recoil
    
    @property
    def heal(self):
        return self._heal
    
    @property
    def critRatio(self):
        return self._critRatio
    
    @property
    def drain(self):
        return self._drain
    
    @property
    def forceSwitch(self):
        return self._forceSwitch
    
    @property
    def selfBoost(self):
        return self._selfBoost
    
    @property
    def weather(self):
        return self._weather
    
    @property
    def additionalEffects(self):
        return self._additionalEffects
    
    # Methods
    def use(self):
        if self._pp == 0:
            raise ValueError(f'{self._name} has no PP left!')
        else:
            self._pp -= 1
        return self._power
    
    def __str__(self):
        return f'''
        Name: {self._name}
        Type: {self._type}
        Category: {self._category}
        Power: {self._power if self._power == self._basePower else f'{self._power} (base: {self._basePower})'}
        Accuracy: {self._accuracy}
        PP: {self._pp}/{self._base_pp}
        Priority: {self._priority}
        Target: {self._target}
        '''