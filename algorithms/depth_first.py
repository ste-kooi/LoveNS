import copy
from classes.model import Model
from classes.station import Station
from classes.route import Route
from classes.connection import Connection


class Depth_first_route:
    def __init__(self, model: Model, route: Route) -> None:
        """
        loads in the model and the route that needs to be changed. 
        Max_time is dependent of the given model and determines the maximum length of the routes.
        Options holds all of the possible options for the route.
        Best_solution holds the calculated score
        
        PARAMETERS
        -----------
        model: Model 
        route: Route
            route moet minimaal een beginstation bevatten
        max_time: int
            afhankelijk van het model dat is ingeladen
        
        """
        self.model = model
        self.best_route = route
        self.max_time = self.model.max_time

        self.options: list[Route] = [self.best_route]
        self.best_solution = 0

    def make_children(self, current_route: Route) -> None:
        """
        Generates the next options for routes. Takes current_route and adds possible stations 
        to the route and appends them individually to the options list. possible stations are
        determined using de last station in the stationslist of the route. It is not possible
        a connection that was previously used in the same route.
        
        PARAMETERS
        ------------------
        current_route: Route
            current_route is a route with at least 1 station
        """
        current_station = current_route.get_stations()[-1]
        possible_connections: dict[str, Connection] = current_station.get_connections()
        for station in possible_connections.keys():
            if not current_route.check_connection(possible_connections[station]):
                continue
            new_station = self.model.stations[station]
            route_option = copy.deepcopy(current_route)
            route_option.add_station(new_station)
            self.options.append(route_option)
    
    def get_next_option(self) -> Route:
        """
        returns the last route option from the optionslist
        """
        return self.options.pop()
    
    def check_score(self) -> bool:
        """
        Calculates the score of the entire model and compares it to best_solution.
        If score is higher the score and the route are saved in best_score and best_route
        """
        score = self.model.calculate_score()
        if score > self.best_solution:
            self.best_solution = score
            print(f"new best score: {self.best_solution}")
            return True
        return False
    
    def run(self) -> Model: 
        """
        Takes a route of the options list as long as there are options. 
        Checks if route is shorter than max_time
        If so, makes children, add it to the model and checks score of model
        Removes route from model and adds the best_route
        Returns the complete model
        """           
        while self.options:   
            current_route = self.get_next_option()
            
            if current_route.duration < self.max_time:
                self.make_children(current_route)
                self.model.add_excisting_route(current_route)
                
                if self.check_score():
                    self.best_route = current_route
                    
                self.model.remove_route(current_route.train_id)
                self.model.add_excisting_route(self.best_route)
        
        return self.model
