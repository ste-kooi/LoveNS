from connection import Connection
from station import Station
from typing import List
import random

class Route:
    
    def __init__(self, station: set, train_id: int) -> None:
        self.station: set = station

        self.duration: int = 0

        self.train_id: int = f"train_{self.train_id}"

        self.route: List[Type[Station]] = []


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
    
        current_station = random.choice(self.station())
        duration = 0

        for x in self.station:
            self.route.append(current_station)
            current_station = random.choice(current_station.connections)
            duration += current_station.connections[2]
            print(self.route)


            if duration > 120:
                self.route = self.route[:-1]
                return True
            
        print("test")
        pass



    def calc_duration(self) -> bool:
        """ 
        Calculates the time that a traject takes. Returns true if the traject is below the max time, else false. 
        
        """

        #TODO
        traject_duraction = 0
        
        self.duration = traject_duraction
        pass


    def comp_traject(self) -> bool:
        """ 
        Compares valiable trajects to determine best option
    
        ."""
        pass

    def add_station(self, ) -> None:
        pass
