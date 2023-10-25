"""
Test class for Tree and Oak class
"""
from abc import ABC, abstractmethod
from datetime import timedelta, datetime

from treevolution.models.tree import Tree
from treevolution.context import Context
from treevolution.models.trees.oak import Oak
from treevolution.world import World

class TestOak:
    """TestOak class in order to test Oak behavior
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
        
        oak.height=6
        assert oak.height == 6

        assert oak.height >= oak.MIN_HEIGHT
        assert oak.height <= oak.MAX_HEIGHT

        
    def test_oak_width(self):
        """Test that the width property is abstract """

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

    def test_oak_health_property(self):
        """
        Test oak health property
        """
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        oak._nutrient = 100  
        assert oak.health == 100  

    
    def test_oak_fallen_property(self):
        """
        Test oak fallen property
        """
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        oak._fallen = False  
        assert oak.fallen == False 

    
    def test_oak_fallen_setter(self):
        """
        Test oak fallen setter
        """
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        oak.fallen = True
        assert oak.fallen == True

    
    def test_oak_fallen_getter(self):
        """
        Test oak fallen getter
        """
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        oak._fallen = False
        assert oak.fallen == False         
        

class TestTree:
    """TestTree class in order to test Tree behavior
    """
    def test_tree(self):
        """Test that a Tree object is created with the correct attributes"""
        coordinate = (0, 0)
        birth = datetime.now()

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        tree = Tree(coordinate, birth, world1)
        assert tree._coordinate == coordinate
        assert tree._birth == birth
        assert tree._world == world1
        assert tree._specie == "Tree"
        assert tree._nutrient == 100
        assert tree._fallen == False
        assert tree._age == 0
        assert tree._days_in_humus == None