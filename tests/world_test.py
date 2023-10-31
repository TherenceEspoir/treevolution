"""
Test class for World class
"""
from datetime import timedelta, datetime
from treevolution.models.tree import Tree
from treevolution.models.trees.oak import Oak
from typing import List
from treevolution.world import World
from treevolution.base import Point

class TestWorld:
    """TestWordl class in order to test World behavior
    """

    #Tester le constructeur
    def test_world(self):
        """Test the constructor method of World
        """
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        
        world1 = World(100, 80, date)
        
        assert world1._height == 100
        assert world1._width == 80
        assert world1._start_date == date

    #Tester la méthode step
    def test_step(self):
        """Test the step method of World
        """
        w_world, h_world = 200, 200
        date_test = datetime(2022,9, 10)
        
        world = World(h_world, w_world, date_test)
        for _ in range(2):
            point = Point.random(w_world, h_world)
            tree = Oak(point, date_test, world)

        world.add_tree(tree)

        list_of_tree: List[Tree] = []
        dat=None
        for _ in range(1000):
            day, _, trees = world.step()
            list_of_tree=trees
            dat=day

        assert dat == date_test + timedelta(days=1000)
        for tree in list_of_tree:
            assert tree._age == 2

        #vérifiez la suppression d’un arbre une fois son âge maximal atteint et sa transition en état humus effectuée
        
