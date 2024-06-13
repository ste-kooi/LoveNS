from classes.model import Model
import random


class Greedy():

    def create_greedy(self):

        route_nr = 1
        route_dur = 0
        # pick a random station from station dict in Model class
        mod = Model("Holland")
        random_station = random.choice(list(mod.stations.values()))
        start_station = random_station
        print(random_station)

        # put the station in route 'n'
        mod.add_route(start_station, route_nr)
        print(mod.routes)

        # got into the connections of that station

        # check what connection has the shortest duration

        # go to that station

        # put that station in route 'n'

        # repeat until 120min has been reached
