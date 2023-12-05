import random
from treevolution.models.branch.branch import Branch

class OakBranch(Branch):
    """
    OakBranch class in order to represent a branch of an oak
    """

    MIN_LEAVES_DENSITY = 0.05
    MAX_LEAVES_DENSITY = 0.1

    MIN_LENGTH = 1
    MAX_LENGTH =2.5


    def __init__(self,height,angle,birth,tree,state,length):
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
    
