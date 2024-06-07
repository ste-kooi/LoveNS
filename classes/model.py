from station import Station
from connection import Connection
from route import Route
import random


class Model:

    def __init__(self, mapname) -> None:
        """
        Constructs a new Model object by loading stations and connections from CSV files.

        Parameters
        ----------
        mapname : str
            The name of the map used to locate the CSV files.
        """
        self.stations: dict[Station] = {}
        self.connections: dict[Connection] = {}
        self.routes: dict[int] = {}
        self.load_stations(mapname)
        self.load_connections(mapname)

    def load_stations(self, mapname):
        """
        Loads stations from a CSV file into the model.

        Parameters
        ----------
        mapname : str
            The name of the map used to locate the CSV file.
        """

        # open file and read every row
        with open(f"source/Stations{mapname}.csv") as stationfile:
            while True:
                stationdata = stationfile.readline().strip().split(",")
                if stationdata[0] == "station":
                    continue
                
                if len(stationdata) == 1:
                    return

                # add every station to self.stations
                                                             # naam            x                     y
                self.stations[stationdata[0]] = ((Station(stationdata[0], float(stationdata[2]), float(stationdata[1]))))

    def load_connections(self, mapname):
        """
        Loads connections from a CSV file into the model and into the stations.

        Parameters
        ----------
        mapname : str
            The name of the map used to locate the CSV file.
        """

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


    def add_route(self, start_station: Station, route_id: int):
        """
        This function adds a route to the model. 

        Parameters
        ----------
        start_station : Station
            The starting station of the route.
        route_id : int
            The unique identifier for the route.
        """
        route = Route(route_id)
        route.add_station(start_station)
        self.routes[route_id] = route

    def remove_route(self, route_id: int):
        """
        This function removes a route from the model. 

        Parameters
        ---------
        route_id : int
            The unique identifier for the route.
        """
        del self.routes[route_id]

                
    def get_coverage(self):
        """
        Calculates the fraction of covered connections.

        Returns
        -------
        float
            The fraction of connections covered by the routes.
        """
        #TODO

        return .9
        
    def total_time(self):
        """
        Calculates the total time of all routes.

        Returns:
            int: The total duration of all routes.
        """
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

        Returns:
            float: K score of the model

        """
        T = len(self.routes)
        p = self.get_coverage()
        Min = self.total_time()
        return p * 1000 - (T * 100 + Min)
    
        # get a sation class

    def make_routes(self):
        """
        Generates random routes for the model, ensuring each route does not exceed 120 minutes.

        -- dit gaat uiteindelijk naar algorithms --
        """
        for train_id in range(7):
            random_station_name = random.choice(list(self.stations.keys()))
            current_station = self.stations[random_station_name]
            self.add_route(current_station, train_id)
            
            while self.routes[train_id].duration < 120:
                random_connection = random.choice(list(current_station.connections.keys()))
                new_connection = current_station.connections[random_connection]
                current_station = new_connection.station2
                    
                self.routes[train_id].add_interconnection(new_connection)
                self.routes[train_id].add_station(current_station)

if __name__ == '__main__':
    pass

    
    