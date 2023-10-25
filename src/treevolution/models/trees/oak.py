import random
from treevolution.models.tree import Tree

class Oak(Tree):
    """
    Oak class in order to represent an oak
    """
    
    MIN_HEIGHT, MAX_HEIGHT = 5, 7
    MIN_AGE, MAX_AGE = 5, 10

    def __init__(self, coordinate, birth, world):
        super().__init__(coordinate, birth, world)
        self._max_age = random.randint(Oak.MIN_AGE, Oak.MAX_AGE)
        self._height = random.randint(Oak.MIN_HEIGHT, Oak.MAX_HEIGHT) 

    
    def evolve(self,context):
        """
        Method evolve qui fait évoluer l’arbre en fonction de sa taille max
        """
        if self.height < self.MAX_HEIGHT:
            self.setHeight=self.height+0.005

        
    @property
    def health(self):
        """
        Method health
        """
        return self.nutrient

    
    @property
    def width(self):
        """
        Method width
        """
        return self.height * 0.08
    


            
