"""
Test class for Tree and Oak class
"""
from abc import ABC, abstractmethod
from datetime import timedelta, datetime
import random
from treevolution.base.geometry import Point
from treevolution.context.weather import Weather
from treevolution.models.state import BranchState


from treevolution.models.tree import Tree
from treevolution.context import Context
from treevolution.models.trees.oak import Oak
from treevolution.world import World
from treevolution.models.branch.branch import Branch

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


    def test_max_age(self):
        """Test the max_age property"""

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        assert oak.world == world1

        assert oak.max_age >= Oak.MIN_AGE
        assert oak.max_age <= Oak.MAX_AGE



    def test_height(self):
        """Test the height property """

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)
        point = Point.random(200,200)
        oak = Oak(point, datetime.now(), world1)
        assert oak.world == world1
        
        assert oak.height == 0
        assert oak.height <= Oak.MAX_HEIGHT

        
    def test_width(self):
        """Test width property"""

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        assert oak.world == world1

        assert oak.width == oak.height * 0.08

       

    def test_evolve(self):
        """Teste que la méthode evolve de  Oak fonctionne correctement"""
        date = datetime.strptime("2022-09-10", "%Y-%m-%d")
        world1 = World(100, 80, date)
        random.seed(42)
        oak = Oak((0, 0), datetime.now(), world1)
        
        weather = Weather.random(world1.date)
        context = Context(weather,10,0)

        oak.evolve(context)
        
        #verifier que le nutriment est entre 0 et 100
        assert oak.nutrient >= 0
        assert oak.nutrient <= 100

        assert oak.height <= Oak.MAX_HEIGHT

        #verifier que lorque l'arbre atteint son age max il viellit et que son nutriment diminue
        oak.age = oak.max_age
        oak.evolve(context)
        assert oak.age == oak.max_age
        assert oak.nutrient < 100
                

    
    def test_health(self):

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        oak._nutrient = 100  
        assert oak.health == 100  

    
    def test_fallen(self):
        """
        Test oak fallen property
        """
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        oak.fallen=False  
        assert oak.fallen == False 

    
    def test_oak_fallen_setter(self):
        """
        Test oak fallen setter
        """
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        oak.fallen=True
        assert oak.fallen == True

    
    def test_oak_fallen_getter(self):
        """
        Test oak fallen getter
        """
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        oak = Oak((0, 0), datetime.now(), world1)
        oak.fallen=False
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
        tree.fallen=True  
        assert tree.fallen == True

    def test_height(self):
        """Test the height property """

        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)

        tree = Tree((0, 0), datetime.now(), world1)
        assert tree.world == world1
        
        assert tree.height == 0
        tree.height=5
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

    def test_radius(self):
        """Test the radius property """

        birth = datetime.now()
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        world1 = World(100, 80, date)
        tree = Tree((0, 0), birth, world1)
        x=tree.radius

    def test_envergure(self):
        """Test the envergure  """

        w_world, h_world = 200, 200
        date_test = datetime(2022,9, 10)
        
        world = World(h_world, w_world, date_test)
        for _ in range(5):
            point = Point.random(w_world, h_world)
            tree = Oak(point, date_test, world)
            world.add_tree(tree)

        list_of_tree= []
        dat=None
        for _ in range(1000):
            day, _, trees = world.step()
            list_of_tree=trees
            dat=day 

        