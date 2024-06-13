from classes.model import Model
from classes.route import Route
import random


class Greedy():

    def create_greedy(self):

        route_nr = 1
        route_dur = 0
        # pick a random station from station dict in Model class
        mod = Model("Holland")
        route = Route(route_nr)
        random_station = random.choice(list(mod.stations.values()))
        start_station = random_station
        print(start_station)


        # put the station in route 'n'
        mod.add_route(start_station, route_nr)
        print(start_station.connections.values())


        # got into the connections of that station
        shortest_con = min(start_station.connections.values(), key=lambda con: con.time)
        print(shortest_con)
        while route_dur < 120:
            if not start_station.connections:
                print(f"No more connections available from {start_station.name}")
                break

            if shortest_con.station1 == start_station:
                destination_station = shortest_con.station2
            else:
                destination_station = shortest_con.station1
            print(f"Shortest connection from {start_station.name} is to {destination_station} with duration {shortest_con.time}")
            route.add_station(destination_station)
            route_dur = route.duration
            print(f"Current route: {route}")
            print(mod.routes)

            start_station = destination_station

            if route_dur >= 120:
                print("Route duration limit reached.")
                break



        # check what connection has the shortest duration

        # go to that station

        # put that station in route 'n'

        # repeat until 120min has been reached
