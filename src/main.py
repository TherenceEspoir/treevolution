"""
Module which enables to simulate a world
"""
from datetime import date, datetime
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
    w_world, h_world = 200, 200

    current_date = date.today()
    date_start = datetime(2022,9, 10) 

    world = World(h_world, w_world, date_start)

    # create trees
    for _ in range(2):
        point = Point.random(w_world, h_world)
        tree = Oak(point, date_start, world)
        world.add_tree(tree)

    # simulate 1000 days    

    list_of_tree: List[Tree] = []
    dat=None
    for _ in range(1000):
        
        #day, _, trees, seeds = world.step()
        day, _, trees = world.step()
        list_of_tree=copy.copy(trees)
        dat=day

    print(f"At {dat}:")
    for tree in list_of_tree:
        print(tree)          


if __name__ == "__main__":
    main()
