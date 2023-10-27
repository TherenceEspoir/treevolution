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
        assert oak.coordinate == coordinate
        assert oak.birth == birth
        assert oak.world == world1
        assert oak.specie == "Oak"
        assert oak.nutrient == 100
        assert oak.fallen == False
        assert oak.age == 0
        assert oak.days_in_humus == None


    def test_oak_max_age(self):
        """Test the max_age property"""

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        assert oak.world == world1

        assert oak.max_age >= Oak.MIN_AGE
        assert oak.max_age <= Oak.MAX_AGE



    def test_oak_height(self):
        """Test the height property """

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        assert oak.world == world1
        
        assert oak.height >= Oak.MIN_HEIGHT
        assert oak.height <= Oak.MAX_HEIGHT

        
    def test_oak_width(self):
        """Test width property"""

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        assert oak.world == world1

        assert oak.width == oak.height * 0.08

       

    def test_oak_evolve(self):
        """Teste que la méthode evolve augmente height de  Oak"""
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        
        context = Context(weather="sunny", sun_intensity=10, humus=5)

        for i in range(3):
            oak.evolve(context)

        assert oak.height >= Oak.MIN_HEIGHT
        assert oak.height <= Oak.MAX_HEIGHT

    
    def test_oak_health_property(self):

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
        oak.setFallen=False  
        assert oak.fallen == False 

    
    def test_oak_fallen_setter(self):
        """
        Test oak fallen setter
        """
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        oak.setFallen=True
        assert oak.fallen == True

    
    def test_oak_fallen_getter(self):
        """
        Test oak fallen getter
        """
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        oak.setFallen=False
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
        assert tree.coordinate == coordinate
        assert tree.birth == birth
        assert tree.world == world1
        assert tree.specie == "Tree"
        assert tree.nutrient == 100
        assert tree.fallen == False
        assert tree.age == 0
        assert tree.days_in_humus == None


    def test_fallen_property(self):
        """
        Test tree fallen property
        """
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)
        tree = Tree((0, 0), datetime.now(), world1)
        assert tree.fallen == False
        tree.setFallen=True  
        assert tree.fallen == True

    def test_height(self):
        """Test the height property """

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        tree = Tree((0, 0), datetime.now(), world1)
        assert tree.world == world1
        
        assert tree.height == 0
        tree.setHeight=5
        assert tree.height == 5

    def test_birth(self):
        """Test the birth property """

        birth = datetime.now()

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)
        tree = Tree((0, 0), birth, world1)
        assert tree.birth == birth

    def test_world(self):
        """Test the world property """

        birth = datetime.now()

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)
        tree = Tree((0, 0), birth, world1)
        assert tree.world == world1    

    def test_nutrient(self):
        """Test the nutrient property """

        birth = datetime.now()

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)
        tree = Tree((0, 0), birth, world1)
        assert tree.nutrient == 100

    def test_age(self):
        """Test the age property """

        birth = datetime.now()

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)
        tree = Tree((0, 0), birth, world1)
        assert tree.age == 0    

    def test_days_in_humus(self):
        """Test the days_in_humus property """

        birth = datetime.now()

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)
        tree = Tree((0, 0), birth, world1)
        assert tree.days_in_humus == None

    def test_specie(self):
        """Test the specie property """

        birth = datetime.now()

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)
        tree = Tree((0, 0), birth, world1)
        assert tree.specie == "Tree"

    def test_max_age(self):
        """Test the max_age property """

        birth = datetime.now()

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)
        tree = Tree((0, 0), birth, world1)
        assert tree.max_age == None    