import copy
from classes.model import Model
from classes.station import Station
from classes.route import Route
from classes.connection import Connection


class Depth_first_route:
    def __init__(self, model: Model, begin_station: Station, train_id: int, max_time: int):
        self.model = copy.deepcopy(model)
        self.best_route = Route(train_id)
        self.best_route.add_station(begin_station)
        self.options: list[Route] = [self.best_route]
        self.best_solution = 0
        self.max_time = max_time

    def make_children(self, this_route):
        if this_route:
            current_station = this_route.get_stations()[-1]
            possible_connections: set[str] = set(current_station.connections.keys())
            for station in possible_connections:
                if station == current_station.name:
                    continue
                new_station = self.model.stations[station]
                route_option = copy.deepcopy(this_route)
                route_option = route_option.add_station(new_station)
                self.options.append(route_option)
    
    def get_next_option(self):
        return self.options.pop()
    
    def check_score(self):
        score = self.model.calculate_score()
        if score > self.best_solution:
            self.best_solution = score
            print(f"new best score: {self.best_solution}")
            return True
        return False
    
    def run(self):            
        while self.options:    
            this_route = self.get_next_option()
            
            if this_route:
                if this_route.duration < self.max_time:
                    self.make_children(this_route)
                
                    if self.check_score():
                        self.best_route = this_route
                        self.model.remove_route(this_route.train_id)
                        self.model.add_excisting_route(this_route)
        
        return self.best_route
