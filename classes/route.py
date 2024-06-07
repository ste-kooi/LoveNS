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
        self.stations: list[Station] = []
        self.interconnections: list[Connection] = []

        self.duration: int = 0
        self.train_id = train_id
        
    def add_interconnection(self, connection: Connection): 
        self.interconnections.append(connection)
        self.refresh_duration()
        
    def add_station(self, station: Station):
        """
        Adds a station to the route
        
        """
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
        if len(self.stations) >= 1:
            return f"{self.stations[0]} - {self.stations[-1]} no. Stations: {len(self.stations)}"
        return None
