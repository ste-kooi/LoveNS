from connection import Connection

class Station:
    """
    Represents a station in the model
    
    """
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.location = (x, y)
        self.connections: dict[int, Connection] = {}

    def set_connection(self, connection) -> None:
        """
        Adds a connection to this station. 

        """

        connection_id = connection.get_id()
        self.connections[connection.id] = connection

    def __repr__(self) -> str:
        return f'{self.name}'
