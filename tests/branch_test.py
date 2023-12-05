
from datetime import datetime
import random
from treevolution.world import World
from treevolution.base.geometry import Point
from treevolution.models.branch.branch import Branch
from treevolution.models.trees.oak import Oak
from treevolution.models.state import BranchState
from treevolution.models.branches.oak.OakBranch import OakBranch
from treevolution.context import Context
from treevolution.context.weather import Weather



class TestOakBranch:
    def test_constructor(self):
        """Test the constructor method of OakBranch
        """
        
        random.seed(42)
        hauteur= 5
        angle= 90
        date_start= datetime(2022,9, 10)

        world = World(200, 200, date_start)
        arbre= Oak(Point(0,0), date_start, world)
        etat= BranchState.EVOLVE
        longueur= 0
        longueur_max= None
        #densite= 0

        #verfier que la variable de classe MIN_LEAVES_DENSITY est bien initialisée
        assert OakBranch.MIN_LEAVES_DENSITY == 0.05
        assert OakBranch.MAX_LEAVES_DENSITY == 0.1

        #verifier que la variable de classe MIN_LENGTH est bien initialisée
        assert OakBranch.MIN_LENGTH == 1
        assert OakBranch.MAX_LENGTH == 2.5

        branche=  OakBranch(hauteur, angle, date_start, arbre, etat, longueur)

        #verifier que la densité de feuillage est bien compise dans l'intervalle de min et max
        assert OakBranch.MIN_LEAVES_DENSITY <= branche._density <= OakBranch.MAX_LEAVES_DENSITY

        #verifier que la longueur est bien compise dans l'intervalle de min et max
        assert OakBranch.MIN_LENGTH <= branche._max_length <= OakBranch.MAX_LENGTH

        branche.height= 20
        assert branche.height == 20
        assert branche.angle == angle
        assert branche.birth == date_start
        assert branche.tree == arbre
        assert branche.state == etat
        assert branche.length == longueur


    def test_evolve(self):
        """ Test the evolve method of OakBranch """
        hauteur= 5
        angle= 90
        date_start= datetime(2022,9, 10)

        world = World(200, 200, date_start)
        arbre= Oak(Point(0,0), date_start, world)

        etat= BranchState.EVOLVE
        longueur= 0

        branche=  OakBranch(hauteur, angle, date_start, arbre, etat, longueur)

        weather= Weather.random(date_start)
        context= Context(weather,10,0)

        arbre.evolve(context)

        x= 1 - (branche.height / arbre.height)
        assert branche.hratio == x

        branche.evolve(context)

        assert branche.length == longueur +(0.005 * arbre.youth_ratio * branche.hratio)
