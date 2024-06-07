from station import Station
from connection import Connection
from route import Route
import random


class Model:

    def __init__(self, mapname) -> None:
        self.stations: dict[Station] = {}
        self.connections: dict[Connection] = {}
        self.load_stations(mapname)
        self.load_connections(mapname)

        self.routes: dict[int] = {}

    def load_stations(self, mapname):
        # open file and read every row
        with open(f"source/Stations{mapname}.csv") as stationfile:
            while True:
                stationdata = stationfile.readline().strip().split(",")
                if stationdata[0] == "station":
                    continue
                
                if len(stationdata) == 1:
                    return False
                    break

                # add every station to self.stations
                                                             # naam            x                     y
                self.stations[stationdata[0]] = ((Station(stationdata[0], float(stationdata[2]), float(stationdata[1]))))

    def load_connections(self, mapname):
        # open file
        connection_id = 0
        with open(f"source/Connecties{mapname}.csv") as connectionfile:
            while True:
                connectiondata = connectionfile.readline().strip().split(",")
                if connectiondata[0] == "station1":
                    continue
                
                if len(connectiondata) == 1:
                    return False

                stationname1 = connectiondata[0]
                stationname2 = connectiondata[1]
                time = int(connectiondata[2])

                # add every connection to self.connections
                connection = Connection(self.stations[stationname1], self.stations[stationname2], time, connection_id)
                self.connections[connection_id] = (connection)
            
                # add every connection to self.stations(station naam)
                self.stations[stationname1].set_connection(connection)
                self.stations[stationname2].set_connection(connection)
                
                connection_id += 1


    def add_route(self, start_station, route_id: int):
        """
        This function adds a route to the model. Needs a starting station and route id

        
        """
        route = Route(route_id)
        route.add_station(start_station)
        self.routes[route_id] = route


                
    def get_coverage(self):
        """
        returns how much of the connections are covered. 
        Kan aan de hand van connections_id, zo kom je niet in de knoop met de richting van de connectie
        """
        #TODO

        return .9
        
    def total_time(self):
        duration = 0
        for route in self.routes.values():
            duration += route.duration
        return duration
            
    
    def calculate_score(self) -> float:
        """
        This function calculates a K score from the model following the formula:

        K = p * 1000 - (T * 100 + Min)

        K:   quality of route planning
        p:   fraction of covered connections
        T:   number of routes
        Min: total minutes of routes

        """
        T = len(self.routes)
        p = self.get_coverage()
        Min = self.total_time()
        return p * 1000 - (T * 100 + Min)
    
        # get a sation class

    def make_routes(self):
        for train_id in range(7):
            first_station_random = random.randint(0, 28)
            current_station = random.choice(list(self.stations.values()))
            self.routes[train_id] = Route(current_station, train_id)
            
            while self.routes[train_id].duration < 120:
                new_connection = random.choice(list(current_station.connections.values()))
                current_station = new_connection.station2
                
                self.routes[train_id].add_interconnection(new_connection)
                self.routes[train_id].add_station(current_station)



if __name__ == '__main__':
    pass    
    

    
    