class Connection:

    def __init__(self, station1: str, station2: str, duration: int, connection_id: int) -> None:
        self.station1: Station = station1
        self.station2: Station = station2
        self.time: int = duration
        self.connection_id = connection_id
    
    def  __repr__(self) -> str:
        return f'{self.connection_id}: {self.station1} - {self.station2}'
