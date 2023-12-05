import random
from treevolution.models.branch.branch import Branch
from treevolution.models.tree import Tree

class OakBranch(Branch):
    """
    OakBranch class in order to represent a branch of an oak
    """

    MIN_LEAVES_DENSITY = 0.05
    MAX_LEAVES_DENSITY = 0.1

    MIN_LENGTH = 1
    MAX_LENGTH =2.5


    def __init__(self,height,angle,birth,tree:Tree,state,length):
        """
        Constructor of OakBranch class
        """
        super().__init__(height,angle,birth,tree,state,length)
        self._density= random.uniform(OakBranch.MIN_LEAVES_DENSITY, OakBranch.MAX_LEAVES_DENSITY)
        self._max_length= random.uniform(OakBranch.MIN_LENGTH, OakBranch.MAX_LENGTH)

    @property
    def height(self):
        """
        Getter for height
        """
        return self._height
    
    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        self._height = value
    
    @property
    def angle(self):
        """
        Getter for angle
        """
        return self._angle
    
    @property
    def birth(self):
        """
        Getter for birth
        """
        return self._birth
    
    @property
    def tree(self):
        """
        Getter for tree
        """
        return self._tree
    
    @property
    def state(self):
        """
        Getter for state
        """
        return self._state
    
    @property
    def length(self):
        """
        Getter for length
        """
        return self._length
    
    @property
    def max_length(self):
        """
        Getter for max_length
        """
        return self._max_length
    
    @property
    def density(self):
        """
        Getter for density
        """
        return self._density
    
    @property
    def hratio(self):
        """
        Getter for hratio
        """
        return 1 - (self.height / self.tree.height)

    def evolve(self,context):
        """
        Method evolve qui fait évoluer la branche
        """
        self._length += 0.005 * self.tree.youth_ratio * self.hratio
