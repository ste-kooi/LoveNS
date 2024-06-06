from typing import List

class Station:
    
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.location = (x, y)
        self.connections: List[(Station, int)] = []

    def set_connection(self, station, duration: int) -> None:
        self.connections.append(station, duration)
        pass

    def __repr__(self) -> str:
        return f'{self.name}'
