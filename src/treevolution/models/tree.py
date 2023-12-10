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
        self._branches = []


    @property
    def branches(self):
        """
        Getter for branches
        """
        return self._branches
    
    @branches.setter
    def branches(self, branches):
        """
        Setter for branches
        """
        self._branches = branches

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
    
    @days_in_humus.setter
    def days_in_humus(self, days_in_humus):
        """
        Setter for days_in_humus
        """
        self._days_in_humus = days_in_humus
        
    
    @property
    def nutrient(self):
        """
        Getter for nutrient
        """
        return self._nutrient
    
    @nutrient.setter
    def nutrient(self, nutrient):
        """
        Getter for nutrient
        """
        self._nutrient = nutrient
    

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

  
    def add_branch(self, branch):
        """
        Method add_branch
        """
        self._branches.append(branch)       

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
        
        if self.state == state.TreeState.HUMUS:
            self.fallen = True
           # return
        #lorsqu’un arbre a atteint son âge maximal, il chute et devient de l’humus

        if (self.age >= self.max_age) and (self.days_in_humus is None):    
            self.fallen = True
            #nombre de jour de humus disponible humus = width *height**2
            self.days_in_humus = self.width * self.height**2
            if self.days_in_humus < 0:
                self.days_in_humus = 0

        if self.fallen == True:
            self._days_in_humus -= 1

    #méthode consumed qui permet de savoir si un arbre à été consumé
    def consumed(self):
        """
        Method consumed
        """
        #considéré comme consumé seulement s’il est fallen et le nombre de jour en stade humus a été atteint ou dépassé
        #print(f'fallen: {self.fallen}, days_in_humus: {self.days_in_humus}')
        if self.fallen==True and (self.days_in_humus <= 0):
            return True
        else:
            return False

    def __str__(self):
        """
        Method __str__
        """
        return f"-- (name : {self.specie}, height : {self.height}, width : {self.width}, coordinate : {self.coordinate.__str__()}, health : {self.health},nutrient : {self.nutrient}, age : {self.age}, max_age : {self.max_age}, humus_day : {self.days_in_humus} ,fallen : {self.fallen} )"
    

    