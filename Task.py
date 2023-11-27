class Task:
    __estimation = 0
    _name = ""
    def __init__(self, name: str, estimation: float):
        self._name = name
        self.__estimation = estimation
    
    def estimation(self):
        return self.__estimation
    
    def name(self):
        return self._name
    
    def __str__(self):
        return "%s: %.2f" % (self._name, self.__estimation)