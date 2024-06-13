import copy
from classes.model import Model

class Depth_first_route:
    def __init__(self, model: Model, mapname: str, begin_station: Station):
        self.model = copy.deepcopy(model)
        self.begin = begin_station
        
        self.states = []
        
        if mapname == "Holland":
            self.amount_trains = 7
            self.timeframe = 120
            
        elif mapname == "Nederland":
            self.amount_trains = 20
            self.timeframe = 180
    
    def make_children(self):
        current_station = self.begin
        possible_connections = list(self.model.connections.keys())
        for station in possible_connecitons:
            self.states.append(station)
    
    def get_next_step(self):
        return 
    
    def check_score(self):
        self.model.calculate_score()
    
    def run(self):
        pass        