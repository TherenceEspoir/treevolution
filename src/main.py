"""
Module which enables to simulate a world
"""
from datetime import date, datetime
import random
from typing import List
from treevolution import World
from treevolution.base import Point
from treevolution.models.tree import Tree
from treevolution.models.trees.oak import Oak
from dateutil.relativedelta import relativedelta
import copy

def main():
    """
    Main function which simulates the world
    """

    """
            À ce stade, si vous simulez une forêt de 5 arbres avec le contexte suivant :
        — La graine aléatoire fixée à 42.
        — Une date de départ fixée à « 2022-09-10 ».
        — Un monde de taille 200 ˆ 200.
        — Les arbres placés aléatoirement.
        — Une simulation de 3000 jours.
    """
    w_world, h_world = 200, 200

    current_date = date.today()
    random.seed(42)

    date_start = datetime(2022,9, 10) 

    world = World(h_world, w_world, date_start)

    # create trees
    for _ in range(5):
        point = Point.random(w_world, h_world)
        tree = Oak(point, date_start, world)
        world.add_tree(tree)

    # simulate 3000 days    

    list_of_tree: List[Tree] = []
    dat=None
    for i in range(1,3001):
        
        day, _, trees = world.step()
        list_of_tree=copy.copy(trees)
        dat=day

        if i % 1000 == 0:
            print(f"At {day}:")
            for tree in list_of_tree:
                print(tree)
            print("\n")
                     


if __name__ == "__main__":
    main()
