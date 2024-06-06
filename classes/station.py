class Station:
    
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.location = (x, y)
        self.connections: dict[int: Station] = {}

    def set_connection(self, connection) -> None:
        self.connections[connection.connection_id] = connection

    def __repr__(self) -> str:
        return f'{self.name}'
