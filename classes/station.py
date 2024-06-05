class Station:
    
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.connections: list[Station] = []

    def make_connections(self) -> None:
        pass

