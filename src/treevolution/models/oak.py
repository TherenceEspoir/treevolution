from treevolution.models.tree import Tree

class Oak(Tree):
    """
    Oak class in order to represent an oak
    """
    #definition de variable de classe
    MIN_HEIGHT, MAX_HEIGHT = 5, 7
    MIN_AGE, MAX_AGE = 5, 10

    def __init__(self, coordinate, birth, world):
        super().__init__(coordinate, birth, world)

    #methode evolve qui fait évoluer l’arbre en fonction de sa taille max 

    @property
    def evolve(self):
        """
        Method evolve
        """
        if self._height < self.MAX_HEIGHT:
            self._height += 0.005





            
