from algorithms.greedy import Greedy
from algorithms.randomise import random_routes
from classes.model import Model

if __name__ == "__main__":
    model = Model("Holland")
    gred = Greedy(model)
    gred.make_route(model)

