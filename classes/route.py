from connection import Connection
from station import Station
import random

class Route:
    
    def __init__(self, train_id: int) -> None:
        self.stations: list[Stations] = []
        self.interconnections: list[Connections] = []

        self.duration: int = 0
        self.train_id = train_id
        
    def add_interconnection(self, connection: Connection): 
        self.interconnections.append(connection)
        self.refresh_duration()
        
    def add_station(self, station: Station):
        self.stations.append(station)
    
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