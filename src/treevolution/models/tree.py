from abc import abstractmethod
from datetime import timedelta, datetime,date
from dateutil.relativedelta import relativedelta
from treevolution.context import Context
from treevolution.models import state

class Tree():
    """
    Tree class in order to represent a tree
    """
    def __init__(self, coordinate, birth, world):
        """
        Constructor of Tree class
        """
        self._coordinate = coordinate
        self._birth = birth
        self._world = world
        self._specie = self.__class__.__name__
        self._height = 0
        self._nutrient = 100
        self._fallen = False
        self._age = 0
        self._max_age = None
        self._days_in_humus = None


    @property
    def state(self):
        """
        Method property state
        """
        if self.age >= self.max_age:
            return state.TreeState.HUMUS
        else:
            return state.TreeState.TREE

    @property
    def coordinate(self):
        """
        Getter for coordinate
        """
        return self._coordinate
    
    @property
    def birth(self):
        """
        Getter for birth
        """
        return self._birth
    
    @property
    def world(self):
        """
        Getter for world
        """
        return self._world
    
    @property
    def specie(self):
        """
        Getter for specie
        """
        return self._specie
    
    @property
    def age(self):
        """
        Getter for age
        """
        return self._age
    
    @age.setter
    def age(self, age):
        """
        Setter for age
        """
        self._age = age
    
    @property
    def max_age(self):
        """
        Getter for max_age
        """
        return self._max_age
    
    @property
    def days_in_humus(self):
        """
        Getter for days_in_humus
        """
        return self._days_in_humus
    
    @property
    def nutrient(self):
        """
        Getter for nutrient
        """
        return self._nutrient
    

    @property
    def fallen(self):
        """
        Getter for fallen
        """
        return self._fallen

    
    @fallen.setter
    def fallen(self, fallen):
        """
        Setter for fallen
        """
        self._fallen = fallen     

    @property
    def height(self):
        """
        Getter for height
        """
        return self._height
    

    @height.setter
    def height(self, height):
        """
        Setter for height
        """
        self._height = height         

    #property abstraite heath qui déterminera en fonction de plusieurs critères propres à l’espèce l’état de santé de l’arbre
    @property
    @abstractmethod
    def health(self):
        """
        Abstract property health
        """
        pass

    @property
    @abstractmethod
    def width(self):
        """
        Abstract property width
        """
        pass
    
    @abstractmethod
    def evolve(self,context: Context):
        """
        Abstract method evolve
        """
        self.age = relativedelta(datetime.now() ,self._birth).years

        if self.state == state.TreeState.HUMUS:
            self.fallen = True
            return

    def __str__(self):
        """
        Method __str__
        """
        return f"-- (name : {self.specie}, height : {self.height}, width : {self.width}, coordinate : {self.coordinate.__str__()}, health : {self.health},nutrient : {self.nutrient}, age : {self.age}, max_age : {self.max_age}, humus_day : {self.days_in_humus} )"
    