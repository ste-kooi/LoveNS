from algorithms.greedy import Greedy
from algorithms.randomise import random_routes
from classes.model import Model

if __name__ == "__main__":
    model = Model("Nederland")
    gred = Greedy(model)
    gred.run(10)

