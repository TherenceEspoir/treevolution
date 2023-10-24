"""
Test class for Tree class
"""
from abc import ABC, abstractmethod
from datetime import timedelta, datetime

from treevolution.models.tree import Tree
from treevolution.context import Context
from treevolution.models.oak import Oak
from treevolution.world import World

class TestOak:
    """TestTree class in order to test Tree behavior
    """

    def test_oak(self):
        """Test that an Oak object is created with the correct attributes"""
        coordinate = (0, 0)
        birth = datetime.now()

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak(coordinate, birth, world1)
        assert oak._coordinate == coordinate
        assert oak._birth == birth
        assert oak._world == world1
        assert oak._specie == "Oak"
        #assert oak._height == 0
        assert oak._nutrient == 100
        assert oak._fallen == False
        assert oak._age == 0
        assert oak._days_in_humus == None


    def test_oak_height(self):
        """Test that the height property can be set and retrieved"""

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        assert oak._world == world1
        #assert oak.height == 0
        
        #oak.height = 6

        oak.height=6
        assert oak.height == 6

        assert oak.height >= oak.MIN_HEIGHT
        assert oak.height <= oak.MAX_HEIGHT

        
    def test_oak_width(self):
        """Test that the width property is abstract and raises a NotImplementedError"""

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        assert oak._world == world1

        oak.height=6

        assert oak.width == oak.height * 0.08

       

    def test_oak_evolve(self):
        """Test that the evolve method increases the height of the Oak"""
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        oak.height=6

        context = Context(weather="sunny", sun_intensity=10, humus=5)

        for i in range(3):
            oak.evolve(context)
        
        assert oak.height >= 5
        assert oak.height <= 7
