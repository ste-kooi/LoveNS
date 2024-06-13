from classes.station import Station
from classes.connection import Connection
from classes.route import Route
import random
from typing import Dict


class Model:

    def __init__(self, mapname: str) -> None:
        """
        Constructs a new Model object by loading stations and connections from CSV files.

        Parameters
        ----------
        mapname : str
            The name of the map used to locate the CSV files.
        """
        self.mapname: str = mapname
        self.stations: Dict[str, Station] = {}
        self.connections: Dict[int, Connection] = {}
        self.used_connections = set()
        self.routes: Dict[int, Route] = {}
        self.load_stations(mapname)
        self.load_connections(mapname)

    def __repr__(self):
        """
        Only for printing DELETE LATER.

        """
        s=""
        s+='self.stations:'+str(self.stations)+'\n'
        s+='self.connections:'+str(self.connections)+'\n'
        s += 'self.routes:'+str(self.routes)+'\n'
        return s

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
                time = float(connectiondata[2])

                # add every connection to self.connections
                connection = Connection(self.stations[stationname1], self.stations[stationname2], time, connection_id)
                self.connections[connection_id] = connection
            
                # add every connection to self.stations(station naam)
                self.stations[stationname1].set_connection(connection)
                self.stations[stationname2].set_connection(connection)
                
                connection_id += 1


    def get_station(self, station_name):
        """
        Returns a station from the model
        
        """
        return self.stations[station_name]
    

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

    def get_route(self, route_id):
        """
        Returns a route from the model
        
        """
        return self.routes[route_id]
                
    def get_coverage(self):
        """
        Calculates the fraction of covered connections.

        Returns
        -------
        float
            The fraction of connections covered by the routes.
        """
        used_connections = set()
        
        # Loop over every route
        for route in self.routes.values():
            # Add unique connections from route.interconnections to used_connections
            used_connections.update(route.interconnections)
        
        # Number of used connections
        used_count = len(used_connections)
        
        # Total number of connections in the model
        total_connections = len(self.connections)
        
        # Return the fraction of used connections / total connections
        if total_connections == 0:
            return 0  
        return used_count / total_connections

        
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
        return p * 10000 - (T * 100 + Min)

    
        # get a sation class
    def get_stations_unused_connections(self):
        """
        Checks the model for stations that still have unused connections.
        Returns a list of station names.
        
        """
        return [station for station in self.stations if any(
        conn not in self.used_connections for conn in self.stations[station].connections.values()
        )]

    def update_used_connections(self, route_id):
        """
        Checks all connections in a route and joins them with the model used connections set.
        
        """

        self.used_connections = self.used_connections.union(self.routes[route_id].interconnections)

    def clear_routes(self):
        """
        Empties the routes and used_connections

        """
        self.routes = {}
        self.used_connections = set()


        
    
    