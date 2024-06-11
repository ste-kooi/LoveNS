class Connection:
    """
    A class to represent a connection between two stations.

    ...

    Attributes
    ----------
    station1 : str
        The name of the first station.
    station2 : str
        The name of the second station.
    time : int
        The duration of the connection in minutes.
    connection_id : int
        The unique identifier for the connection.
    """
    def __init__(self, station1: str, station2: str, duration: int, connection_id: int) -> None:
        
        self.station1: str = station1
        self.station2: str = station2
        self.time: int = duration
        self.connection_id: int = connection_id

    def get_id(self):
        return self.connection_id
    
    def  __repr__(self) -> str:
        return f'{self.station1} - {self.station2}'
