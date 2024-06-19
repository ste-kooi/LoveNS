from algorithms.greedy import Greedy
from classes.model import Model

if __name__ == "__main__":
    model = Model("Holland")
    gred = Greedy(model)
    gred.make_route(model)

