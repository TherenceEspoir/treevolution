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


#methode step qui avance la date d'un jour

    def step(self):
        """
        Method qui avance la date d'un jour
        """
        self._start_date = self._start_date + datetime.timedelta(days=1)

#methode date qui retourne la date courante
    
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
        
