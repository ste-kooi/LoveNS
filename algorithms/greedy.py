from classes.model import Model
from classes.route import Route
import random
import copy


class Greedy():

    def __init__(self) -> None:
        self.route_nr = 1
        self.route_dur = 0

        self.mod = Model("Holland")
        self.route = Route(self.route_nr)
        self.temp_route = copy.copy(Route(self.route_nr))

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


            print(self.route)
            print(self.temp_route)


