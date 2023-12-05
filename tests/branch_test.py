
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

        """
        — Une hauteur (height), qui détermine son emplacement sur le tronc de l’arbre.
        — Un angle de position sur le tronc, déterminant son orientation.
        — Une date de naissance (birth).
        — L’instance d’arbre associée.
        — Un état de type models.state.BranchState par défaut fixé à EVOLVE.
        — Une longueur (length), qui définit sa taille (par défaut fixée à 0).
        — Une longueur maximale (max_length) fixée à None pour le moment.
        — Une densité de feuillage (density) fixée à 0 également.
        — Une méthode evolve abstraite qui déterminera par la suite comment évolue la branche. Cette
        méthode prend en paramètre un contexte tout comme pour l’évolution d’un arbre.
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

        assert branche.height == hauteur
        assert branche._angle == angle
        assert branche._birth == date_start
        assert branche._tree == arbre
        assert branche._state == etat
        assert branche._length == longueur
        