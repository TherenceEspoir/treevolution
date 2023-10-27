"""
Test class for World class
"""
from datetime import timedelta, datetime

from treevolution.world import World

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
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        
        world1 = World(100, 80, date)
        
        world1.step()
         
        assert world1.date == date + timedelta(days=1)
