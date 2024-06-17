from classes.model import Model
from classes.route import Route
import random


class Greedy():

    def create_greedy(self):

        route_nr = 0
        route_dur = 0
        mod = Model("Holland")
        route = Route(route_nr)
        random_station = random.choice(list(mod.stations.values()))

        for x in range(6):
            route_nr += 1
            mod.add_route(random_station,route_nr)

        print(mod.routes)


