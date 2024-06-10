from connection import Connection
from station import Station
import random

class Route:
    """
    A class to represent a route for a train.

    ...

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
        self.train_id = train_id
        self.stations: list[Station] = []
        self.interconnections: list[Connection] = []
        self.duration: int = 0

    def check_station(self, station: Station):
        """
        Checks if the connecting station and current station are the same.
        """

        connection = Connection()
        
        last_station = self.stations[-1]
        if last_station == connection.station1:
            return False
            print ("test")
        else:
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
                self.interconnections.append(connection)
                # Update the total duration of the route.
                self.duration += connection.time

        # Add the new station to the list of stations in the route.
        self.stations.append(station)

    def remove_station(self, station: Station):
        """
        Removes a station from the route
        
        """
        self.stations.remove(station)
    
    def refresh_duration(self):
        duration = 0
        for interconnection in self.interconnections:
            duration += interconnection.time
        self.duration = duration
        
    def is_valid(self) -> bool:
        """
        Returns if traject duration is below 120 minutes
        """
        return self.duration < 120

    def comp_traject(self) -> bool:
        """ 
        Compares valiable trajects to determine best option
    
        ."""
        pass
    
    def __repr__(self):
        station_names = ' -> '.join([station.name for station in self.stations])
        return f'Route {self.train_id}: {station_names} (Duration: {self.duration} minutes)'