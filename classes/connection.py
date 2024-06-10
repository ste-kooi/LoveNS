class Connection:
    """
    A class to represent a connection between two stations.

    ...

    Attributes
    ----------
    start : Connection (object)
        The connection object of the beginning station (made in model.load_connections())
    destination : Connection (object)
        The connection object of the last station (made in model.load_connections())
    time : int
        The duration of the connection in minutes.
    connection_id : int
        The unique identifier for the connection.
    """
    def __init__(self, station1: Connection, station2: Connection, duration: int, connection_id: int) -> None:
        
        self.start = station1
        self.destination = station2
        self.time: int = duration
        self.connection_id = connection_id
        
    def get_start_station(self):
        return self.start
    
    def get_destination(self):
        return self.destination
        
    def get_id(self):
        return self.connection_id

    def  __repr__(self) -> str:
        return f'{self.station1} - {self.station2}'
