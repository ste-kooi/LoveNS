from classes.connection import Connection
from classes.station import Station
import random

class Route:
    """
    A class to represent a route for a train.

    ...s

    Attributes
    ----------
    stations : list
        A list the stations along the route.
    interconnections : list
        A list of the connections between stations.
    duration : int
        The total duration of the route in minutes.
    train_id : int
        The unique identifier for the train route
    """

    def __init__(self, train_id: int) -> None:
        self.train_id: int = train_id
        self.stations: list[Station] = []
        self.interconnections: set[Connection] = set()
        self.duration: int = 0

    def check_connection(self, connection: Connection):
        """
        Checks if the chosen connection and the used interconnections are the same.

        """
        chosen_interconnection = connection.get_id()
        for interconnection in self.interconnections:
            used_interconnection = interconnection.get_id()
            if chosen_interconnection == used_interconnection:
                return False
        return True

    def add_station(self, station: Station):
        """
        Adds a station and the connection to the route.
        """

            # Check if the route already contains stations.
        if self.stations:
            # Get the last station in the current route.
            last_station = self.stations[-1]
            # Find the connection from the last station to the new station.
            connection = last_station.connections.get(station.name)
            # Check if a valid connection is found.
            if connection:
                # Append the connection to the interconnections list.
                self.interconnections.add(connection)
                # Update the total duration of the route.
                self.duration += connection.time

        # Add the new station to the list of stations in the route.
        self.stations.append(station)

    def remove_last_station(self):
        """
        Removes a station from the route and updates the route total time

        """
        if self.stations:
            # remove last station in the route
            station = self.stations.pop()
            # Get the last station in the resulting route
            if self.stations:
                last_station = self.stations[-1]
                # Find the connection from the last station to the new station.
                connection = last_station.connections.get(station.name)
                # Update duration and remove interconnection
                self.interconnections.discard(connection)
                self.duration -= connection.time

    def get_stations(self):
        """
        Returns all stations from the route

        """
        return self.stations


    def deep_copy_route(self):
        """
        Creates a deep copy of a route.
        """
        new_route = Route(self.train_id)
        new_route.stations = list(self.stations)
        new_route.interconnections = set(self.interconnections)
        new_route.duration = self.duration
        return new_route


    def refresh_duration(self):
        duration = 0
        for interconnection in self.interconnections:
            duration += interconnection.time
        self.duration = duration


    def __repr__(self):
        station_names = ' -> '.join([station.name for station in self.stations])
        return f'Route {self.train_id}: {station_names} (Duration: {self.duration} minutes)'
