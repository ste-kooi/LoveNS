from station import Station
from connection import Connection
from traject import Traject

class Model:
    
    def __init__(self) -> None:
        self.stations: dict[Station] = {}
        self.connections: set[Connection] = set()
        self.load_stations()
        self.load_connections()
        # self.routes: set[Routes] = set()

    def load_stations(self):
        # open file and read every row
        with open("../source/StationsHolland.csv") as stationfile:
            while True:
                stationdata = stationfile.readline().strip().split(",")
                if stationdata[0] == "station":
                    continue
                
                if len(stationdata) == 1:
                    return False
                    break

                # add every station to self.stations
                                                            # naam            x               y
                self.stations[stationdata[0]] = ((Station(stationdata[0], stationdata[2], stationdata[1])))

    def load_connections(self):
        # open file
        with open("../source/ConnectiesHolland.csv") as connectionfile:
            while True:
                connectiondata = connectionfile.readline().strip().split(",")
                if connectiondata[0] == "station1":
                    continue
                
                if len(connectiondata) == 1:
                    return False
                    break

                stationname1 = connectiondata[0]
                stationname2 = connectiondata[1]
                time = connectiondata[2]

                # add every connection to self.connections
                self.connections.add(Connection(stationname1, stationname2, time))
            
                # add every connection to self.stations(station naam)
                self.stations[stationname1].set_connection(Connection(stationname1, stationname2, time))
                self.stations[stationname2].set_connection(Connection(stationname2, stationname1, time))

    def total_time(self):
        totaltime = 0
        for route in self.routes:
            totaltime += route.duration
        return totaltime
    
    def make_route(self):
        # TODO make algorithm
        pass
    
    
    

    
    