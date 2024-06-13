from classes.connection import Connection
from typing import Dict

class Station:
    """
    Represents a station in the model
    
    """
    def __init__(self, name: str, x: float, y: float) -> None:
        self.name: str = name
        self.location: tuple[float, float] = (x, y)
        self.connections: Dict[str, Connection] = {}

    def set_connection(self, connection) -> None:
        """
        Adds a connection to this station. 

        """
        if connection.station1 == self:
            destination = connection.station2
        else:
            destination = connection.station1
        
        self.connections[destination.name] = connection

    def __repr__(self) -> str:
        return f'{self.name}'
