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

    
    def evolve(self,context):
        """
        Method evolve
        """

        if self._height < self.MAX_HEIGHT:
            self._height += 0.005

        

    @property
    def health(self):
        """
        Method health
        """
        return self._nutrient

    #la largeur du tronc est quand à elle définie par : height* 0.08
    @property
    def width(self):
        """
        Method width
        """
        return self._height * 0.08

   


            
