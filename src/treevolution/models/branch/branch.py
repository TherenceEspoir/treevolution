from abc import ABC, abstractmethod

from treevolution.models.tree import Tree
from treevolution.models import state

class Branch(ABC):
    def __init__(self,height,angle,birth,tree:Tree):
        self._height= height
        self._angle= angle
        self._birth= birth
        self._tree= tree
        self._state= state.BranchState.EVOLVE
        self._length = 0
        self._max_length= None
        self._density= 0