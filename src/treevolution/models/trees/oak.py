import random
import secrets
from treevolution.models.tree import Tree
from treevolution.models import state
from treevolution.context import Context
from treevolution.context.weather import Weather
from treevolution.models.branches.oak.OakBranch import OakBranch

from datetime import timedelta, datetime

class Oak(Tree):
    """
    Oak class in order to represent an oak
    """
    
    MIN_HEIGHT, MAX_HEIGHT = 5, 7
    MIN_AGE, MAX_AGE = 5, 10
    PERCENT_BEFORE_BRANCH = 0.2

    def __init__(self, coordinate, birth, world):
        super().__init__(coordinate, birth, world)
        self._max_age = random.uniform(Oak.MIN_AGE,Oak.MAX_AGE)
        self.max_height = random.uniform(Oak.MIN_HEIGHT,Oak.MAX_HEIGHT)
        
    def evolve(self,context : Context):
        """
        Method evolve qui fait évoluer l’arbre en fonction de sa taille max
        """
        super().evolve(context)
        #si un arbre est en état humus, il ne peut pas évoluer
        if self.state == state.TreeState.HUMUS:
            return
        else:
            if self.height < self.max_height:
                self.height=self.height + (0.005* self.youth_ratio)
            self.nutrient = self.nutrient - 0.2
            self.nutrient= self.nutrient + context.weather.humidity
            self.nutrient= self.nutrient+( context.humus * context.weather.humidity)
            if self.nutrient < 0:
                self.nutrient = 0
            elif self.nutrient > 100:
                self.nutrient = 100
                

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
        
    @property
    def youth_ratio(self):
        """
        Method youth_ratio qui fournit un ratio de jeunesse d’un arbre déterminé par : 1-(age/age**max)
        """
        return 1-(self.age /self.max_age)
    
    def createBrancheOak(self,context : Context):
        """
        Method createBranchesOak qui crée une branche d’un arbre oak
        """
        #nombre aléatoire entre 0 et 1 (inclus)
        nombre_random = random.uniform(0, 1)

        #probabilité souhaitée (2% , soit 0.02)
        probabilite = 0.02

        if nombre_random <= probabilite :
            if context.energy > 0.2 and self.health > 50:
                height = random.uniform(self.height * Oak.PERCENT_BEFORE_BRANCH ,self.height)
                angle = random.uniform(0,360)
                branch = OakBranch(height, angle, self.birth, self, 0)
                self.nutrient -= 5
                self.add_branch(branch)
                return branch
            return None
        return None
