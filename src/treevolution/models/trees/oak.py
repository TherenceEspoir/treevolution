import random
import secrets
from treevolution.models.tree import Tree
from treevolution.models import state

class Oak(Tree):
    """
    Oak class in order to represent an oak
    """
    
    MIN_HEIGHT, MAX_HEIGHT = 5, 7
    MIN_AGE, MAX_AGE = 5, 10

    def __init__(self, coordinate, birth, world):
        super().__init__(coordinate, birth, world)
        self._max_age = random.uniform(Oak.MIN_AGE,Oak.MAX_AGE)
        self._height = random.uniform(Oak.MIN_HEIGHT,Oak.MAX_HEIGHT)
        
    def evolve(self,context):
        """
        Method evolve qui fait évoluer l’arbre en fonction de sa taille max
        """
        super().evolve(context)
        #si un arbre est en état humus, il ne peut pas évoluer
        if self.state == state.TreeState.HUMUS:
            return
        else:
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
    