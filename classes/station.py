class Station:
    
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.location = (x, y)
        self.connections: list[Station] = []

    def make_connections(self) -> None:
        pass

