import copy
from classes.model import Model

class Depth_first_route:
    def __init__(self, model: Model, mapname: str, begin_station: Station):
        self.model = copy.deepcopy(model)
        self.begin = begin_station
        
        self.options = []
        self.best_trains: dict[int, list[Route]] #int is train_id
        
        if mapname == "Holland":
            self.amount_trains = 7
            self.timeframe = 120
            
        elif mapname == "Nederland":
            self.amount_trains = 20
            self.timeframe = 180
    
    def make_children(self, station):
        current_station = self.begin
        possible_connections: list[str] = list(current_station.connections.keys())
        for station in possible_connecitons:
            self.options.append(station)
    
    def get_next_step(self):
        return self.states.pop()
    
    def check_score(self):
        self.model.calculate_score()
    
    def run(self):
        for train_id in range(1, amount_trains + 1):
            self.best_trains[train_id] = []
            new_route = self.model.add_route(self.begin, train_id)
            self.make_children(self.begin)
            
            while self.options and new_route.duration < 120:
                
                # route moet herbruikt worden en dan met een station toevoegen om alle mogelijkheden te onderzoeken