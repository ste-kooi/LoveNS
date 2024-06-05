class Connection:

    def __init__(self, station1: str, station2: str, duration: int) -> None:
        self.station1: str = station1
        self.station2: str = station2
        self.time: int = duration
