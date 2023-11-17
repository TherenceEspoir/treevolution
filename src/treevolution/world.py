import random
from typing import List
from treevolution.models.tree import Tree
from treevolution.context import Context
from datetime import timedelta, datetime
from datetime import date
from dateutil.relativedelta import relativedelta

import datetime
"""
Module which contains World class
"""

class World():
    """
    World class in order to represent the forest and simulate the evolution of trees
    """
    def __init__(self, height, width, start_date):
        """
        Constructor of World class
        """
        self._height = height
        self._width = width
        self._start_date = start_date
        self._list_of_tree: List[Tree] = []

    
    @property
    def list_of_tree(self):
        return self._list_of_tree

    def step(self):
        """
        Method qui avance la date d'un jour et simule l'ensemble des arbres
        """
        self._start_date = self._start_date + timedelta(days=1)

        random.seed(42)
        weather_options = ["ensoleillé", "nuageux", "pluvieux", "neige", "orage"]

        weather = random.choice(weather_options)

        context = Context(weather,None,10)

        for tree in self._list_of_tree:
            tree.evolve(context)
            tree.age= relativedelta(self._start_date ,tree._birth).years
            #lorsqu’un arbre est consumé, il est supprimé de la représentation du monde
            if tree.consumed()==True:
                self._list_of_tree.remove(tree)
               
  
        self._weather = weather
        return (self._start_date, weather, self.list_of_tree)
        
        
    def state(self):
        """
        Method qui retourne l'état du monde sans simuler
        """
        return (datetime.now(), self._height,self._width, self.list_of_tree)
    
    @property
    def date(self):
        """
        Method qui retourne la date courante
        """
        return self._start_date
    
    @property
    def height(self):
        """
        Method qui retourne la hauteur
        """
        return self._height
    
    @property
    def width(self):
        """
        Method qui retourne la largeur
        """
        return self._width
        
    
    def add_tree(self, tree):
        """
        Method qui ajoute un arbre à cette liste des arbres connus
        """
        self._list_of_tree.append(tree)