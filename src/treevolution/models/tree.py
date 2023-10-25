
from abc import abstractmethod


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

    #property abstraites heath qui déterminera en fonction de plusieurs critères propres à l’espèce l’état de santé de l’arbre
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
    
    #methode abstraite evolve
    #cette méthode prend en paramètre un contexte d’environnement (définit dans context.context)

    @abstractmethod
    def evolve(self, context):
        """
        Abstract method evolve
        """
        pass


    #méthode __str__ pour proposer l’affichage d’une instance de la classe
    def __str__(self):
        """
        Method __str__
        """
        return f"{self._specie} : {self._height}m, {self._age} years old, {self._nutrient} health, fallen : {self._fallen}" 

       




    