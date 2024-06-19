from classes.model import Model
from classes.route import Route
from algorithms.randomise import random_routes
import random
import copy

class Greedy():

    def __init__(self, model: Model) -> None:
        self.model = copy.deepcopy(model)
        self.usable_connections = self.model.connections
        self.score = self.model.calculate_score()

    def make_route(self, new_model: Model):
        route_id = 1
        route_dur = 0
        used_connections = set()
        new_station = random.choice(list(new_model.stations.values()))
        print(new_station)

        new_model.add_route(new_station, route_id)
        print(new_model.routes)

        while new_model.routes[route_id].duration < new_model.max_time:
            sorted_connections = sorted(new_station.connections.values(), key=lambda con: con.time)
            print(sorted_connections)

            best_connection = sorted_connections[0]

            for connection in sorted_connections:
                if connection not in used_connections:
                    best_connection = connection

            if best_connection.station1 == new_station:
                new_station = best_connection.station2
            else:
                new_station = best_connection.station1

            used_connections.add(best_connection)
            new_model.routes[route_id].add_station(new_station)
            new_model.routes[route_id].refresh_duration()

            if new_model.routes[route_id].duration >= 120:
                new_model.routes[route_id].remove_last_station()
                route_id += 1
                used_connections = set()
                break

            print(new_model.routes)












class was_last_version():


    def __init__(self) -> None:
        self.route_nr = 1
        self.route_dur = 0

        self.mod = Model("Holland")
        self.temp_mod = copy.deepcopy(self.mod)
        self.route = Route(self.route_nr)
        self.temp_route = copy.deepcopy(self.route)


    def create_greedy(self):

        for x in range(6):
            self.route_nr += 1
            random_station = random.choice(list(self.mod.stations.values()))
            self.mod.add_route(random_station,self.route_nr)

            while self.mod.routes[self.route_nr].duration < self.mod.max_time:
                sorted_connections = sorted(random_station.connections.values(), key=lambda con: con.time)

                for connection in sorted_connections:
                    if connection.station1 == random_station:
                        destination_station = connection.station2
                    else:
                        destination_station = connection.station1

                    self.route.add_station(destination_station)
                    best_score = self.mod.calculate_score() #hoe vergelijk ik scores?

                    for temp_connection in sorted_connections[1:]: # begint een positie verder zodat je steeds 2 connecties met elkaar vergelijkt.
                        if connection.station1 == random_station:
                            temp_destination_station = connection.station2
                        else:
                            temp_destination_station = connection.station1

                        self.temp_route.add_station(temp_destination_station)
                        temp_best_score = self.mod.calculate_score() #hoe vergelijk ik deze score met best_score

                        if temp_best_score > best_score:
                            best_score = temp_best_score
                            self.route.remove_last_station()
                            self.route.add_station(temp_destination_station)
                            random_station = temp_destination_station
                            break
                        else:
                            random_station = destination_station
                            break










