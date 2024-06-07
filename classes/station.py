from connection import Connection

class Station:
    """
    Represents a station in the model
    
    """
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.location = (x, y)
        self.connections: dict[Connection] = {}

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
