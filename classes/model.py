from classes import Station
from classes import Connection
from typing import List
from typing import Type

class Model:
    
    def __init__(self) -> None:
        self.stations: List[Type[Station]]
        self.connections: List[Type[Connection]]

    def load_stations(self, file):
        
        # open file

        # loop over rows

        # append station to self.stations
        pass

    def load_connections(self, file):

        # open file

        # loop over rows

        # append station to self.connections

        pass
        