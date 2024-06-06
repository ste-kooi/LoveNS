from station import Station
from connection import Connection
from route import Route
import random

class Model:
    
    def __init__(self) -> None:
        self.stations: dict[Station] = {}
        self.connections: set[Connection] = set()
        self.load_stations()
        self.load_connections()

        self.routes: set[Route] = set()

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

    def calculate_score(self) -> float:
        """
        This function calculates a K score from the model following the formula:

        K = p * 1000 - (T * 100 + Min)

        K:   quality of route planning
        p:   fraction of covered connections
        T:   number of routes
        Min: total minutes of routes

        """
        T = len(self.routes)
        p = self.coverage()
        Min = self.total_time()
        return p * 1000 - (T * 100 + Min)
    
    def total_time(self):
        totaltime = 0
        for route in self.routes:
            totaltime += route.duration
        return totaltime
    

    
    def make_routes(self) -> None:
        """ 
        Makes a route 
        
        """

        # get a sation class

        # put that station in a list

        # check the connections from that station and go to one of those stations

        # get that station class

        # put that station in the list

        # repeat
    
        current_station = random.choice(self.stations)
        duration = 0

        while duration < 500:
            self.routes.append(current_station)
            current_station = random.choice(current_station.connections)
            duration += current_station.connections.time
            print(self.routes)


            if duration > 120:
                self.route = self.routes[:-1]
                return True
 
        print("test")


        __name__ == '__main__'

        route = make_routes()

        print(route)
    
    

    
    