from abc import ABC, abstractmethod

class Branch(ABC):
    def __init__(self,height,angle,birth,tree,state,length):
        self._height= height
        self._angle= angle
        self._birth= birth
        self._tree= tree
        self._state= state
        self._length= length
        self._max_length= None
        self._density= 0
        
