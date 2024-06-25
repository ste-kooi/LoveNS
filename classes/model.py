from classes.station import Station
from classes.connection import Connection
from classes.route import Route
import random
from typing import Dict
import copy


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
        self.max_routes: int = 0
        self.max_time: int = 0
        self.stations: Dict[str, Station] = self.load_stations(mapname)
        self.connections: Dict[int, Connection] = self.load_connections(mapname)
        self.routes: Dict[int, Route] = {}
        self.used_connections: set = set()

    def __repr__(self):
        """
        Only for printing DELETE LATER.

        """
        s=""
        s+='self.stations:'+str(self.stations)+'\n'
        s+='self.connections:'+str(self.connections)+'\n'
        s += 'self.routes:'+str(self.routes)+'\n'
        return s

    def load_stations(self, mapname: str):
        """
        Loads stations from a CSV file into the model.

        Parameters
        ----------
        mapname : str
            The name of the map used to locate the CSV file.
        """

        # load model constraints
        if mapname == 'Nederland':
            self.max_routes, self.max_time = 20, 180
        else:
            self.max_routes, self.max_time = 7, 120

        stations = {}
        # open file and read every row
        with open(f"source/Stations{mapname}.csv") as stationfile:
            while True:
                stationdata = stationfile.readline().strip().split(",")
                if stationdata[0] == "station":
                    continue

                if len(stationdata) == 1:
                    return stations

                # add every station to self.stations
                                                             # naam            x                     y
                stations[stationdata[0]] = ((Station(stationdata[0], float(stationdata[2]), float(stationdata[1]))))

    def load_connections(self, mapname: str):
        """
        Loads connections from a CSV file into the model and into the stations.

        Parameters
        ----------
        mapname : str
            The name of the map used to locate the CSV file.
        """

        # open file
        connection_id = 0
        connections = {}
        with open(f"source/Connecties{mapname}.csv") as connectionfile:
            while True:
                connectiondata = connectionfile.readline().strip().split(",")
                if connectiondata[0] == "station1":
                    continue

                if len(connectiondata) == 1:
                    return connections

                stationname1 = connectiondata[0]
                stationname2 = connectiondata[1]
                time = float(connectiondata[2])

                # add every connection to self.connections
                connection = Connection(self.stations[stationname1], self.stations[stationname2], time, connection_id)
                connections[connection_id] = connection

                # add every connection to self.stations(station naam)
                self.stations[stationname1].set_connection(connection)
                self.stations[stationname2].set_connection(connection)

                connection_id += 1


    def get_station(self, station_name: str):
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

    def add_excisting_route(self, excisting_route):
        """
        This function adds an excisting route to the model.
        """
        self.routes[excisting_route.train_id] = excisting_route

    def remove_route(self, route_id: int):
        """
        This function removes a route from the model.

        Parameters
        ---------
        route_id : int
            The unique identifier for the route.
        """
        if route_id in self.routes:
            self.used_connections - self.routes[route_id].interconnections
            del self.routes[route_id]

    def get_route(self, route_id: int):
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
        self.local_used_connections = set()

        # Loop over every route
        for route in self.routes.values():
            # Add unique connections from route.interconnections to used_connections
            for interconnection in route.interconnections:
                self.local_used_connections.add(interconnection.get_id())


        # Number of used connections
        used_count = len(self.local_used_connections)

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
        
    def calculate_score_bonus(self) -> float:
        """
        This function calculates a K score from the model following the formula:

        K = p * 1000 - (T * 100 + Min)

        K:   quality of route planning
        p:   fraction of covered connections
        T:   number of routes
        Min: total minutes of routes
        
        If the coverage is 1, the score will be given a bonus of 100 points

        Returns:
            float: K score of the model

        """
        T = len(self.routes)
        p = self.get_coverage()
        Min = self.total_time()
        
        if p > 0.99:
            return (p * 10000 - (T * 100 + Min)) + 100
        return p * 10000 - (T * 100 + Min)


        # get a sation class
    def get_stations_unused_connections(self):
        """
        Checks the model for stations that still have unused connections.
        Returns a list of station names.

        """
        unused = [station for station in self.stations if any(
        conn not in self.used_connections for conn in self.stations[station].connections.values()
        )]

        if unused:
            return unused
        return list(self.stations.keys())

    def update_used_connections(self):
        """
        Checks all connections in a route and joins them with the model used connections set.

        """
        self.used_connections = set()
        for route_id in self.routes:
            self.used_connections = self.used_connections.union(self.routes[route_id].interconnections)


    def clear_routes(self):
        """
        Empties the routes and used_connections

        """
        self.routes = {}
        self.used_connections = set()

    def copy(self):
        """
        Creates a deep copy of the model, including routes and used_connections.
        """
        new_model = copy.copy(self)
        new_model.routes = {route_id: route.deep_copy_route() for route_id, route in self.routes.items()}
        new_model.used_connections = set(self.used_connections)
        return new_model


