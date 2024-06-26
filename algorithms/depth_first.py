import copy
import time
from classes.model import Model
from classes.station import Station
from classes.route import Route
from classes.connection import Connection
from output.terminal_output import interim_overview, total_overview, missed_connections


class Depth_first_all:
    def __init__(self, model: Model, score = 0) -> None:
        """
        loads in the model and the route that needs to be changed. 
        Max_time is dependent of the given model and determines the maximum length of the routes.
        Options holds all of the possible options for the route.
        Best_solution holds the calculated score
        states holds amout of tested options
        used_begin_station holds all the stations that have been used as a begin station
        
        PARAMETERS
        -----------
        model: Model 
        route: Route
            route moet minimaal een beginstation bevatten
        max_time: int
            afhankelijk van het model dat is ingeladen
        
        """
        self.model = copy.deepcopy(model)
        self.max_routes = self.model.max_routes
        self.max_time = self.model.max_time
        
        self.best_route = None
        self.best_solution = score

        self.options: list[Route] = []
        self.states = 0
        
        self.used_begin_stations = set()

    def add_begin_option(self, train_id: int) -> None:
        """
        Adds a beginning of a route to the self.options list
        
        PARAMETERS
        ------------
        train_id: int
            train_id is the id of the current route to be made
        
        """
        print("ALL STATIONS")
        route = Route(train_id)
        for station in self.model.stations.values():
            if station in self.used_begin_stations:
                continue
            new_option = route.deep_copy_route()
            new_option.add_station(station)
            self.options.append(new_option)
    
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
        # get last station from route
        current_station = current_route.get_stations()[-1]
        # get all connections from station
        possible_connections: dict[str, Connection] = current_station.get_connections()
        for station in possible_connections.keys():
            # check if valid connection, if not skip connection
            if not current_route.check_connection(possible_connections[station]):
                continue
            # retrieve station object from station name
            new_station = self.model.stations[station]
            # copy route option, so not all routes are the same
            route_option = current_route.deep_copy_route()
            route_option.add_station(new_station)
            if route_option.duration < 120:
                self.options.append(route_option)
    
    def get_next_option(self) -> Route:
        """
        returns the last route option from the optionslist
        """
        return self.options.pop()
    
    def check_score(self, coverage: bool) -> bool:
        """
        Calculates the score of the entire model and compares it to best_solution.
        If score is higher the score is saved in best_score
        
        PARAMETERS
        -----------
        Coverage: bool
            a bool given by run(). If True calculate a coverage bonus
        """
        if coverage:
            score = self.model.calculate_score_bonus()
        else:
            score = self.model.calculate_score()
        
        if score >= self.best_solution:
            self.best_solution = score
            return True
        return False
    
    def run(self, coverage = False) -> Model: 
        """
        Takes a route of the options list as long as there are options. 
        Checks if route is shorter than max_time
        If so, makes children, add it to the model and checks score of model
        Removes route from model and adds the best_route
        Returns the complete model
        
        PARAMETERS
        -----------
        coverage: bool
            By default False. But can be turned on if user wants a coverage bonus
        """         
        self.start = time.time()
        
        for train_id in range(1, self.max_routes + 1):
            self.add_begin_option(train_id)
            self.best_route = self.options[-1]
            
            while self.options:
                current_route = self.get_next_option()
                self.states += 1
            
                # check if route is within max_time
                if current_route.duration < self.max_time:
                    self.make_children(current_route)
                    # add route to model for score checking
                    self.model.add_excisting_route(current_route)
                
                    if self.check_score(coverage):
                        # if new high score current_route is best_route
                        self.best_route = current_route
                    
                    #remove current_route from model so there is room to add best_route
                    self.model.remove_route(current_route.train_id)
                    self.model.add_excisting_route(self.best_route)
                    self.end = time.time()
            interim_overview(self.model, train_id)
            
            # remove unused routes and end loop for this train_id
            if len(self.best_route.stations) == 1:
                self.model.remove_route(self.best_route.train_id)
                print(f"Deleted route {train_id}")
                print()
                total_overview(self.model, self.states, self.start, self.end)
                missed_connections(self.model)
                return self.model
                
        total_overview(self.model, self.states, self.start, self.end)
        missed_connections(self.model)
        return self.model

class Depth_first_chosen(Depth_first_all):
    def __init__(self, model: Model) -> None:
        """
        Initialises the depth_first_all __init__() first and then adds begin_stations
        Begin_stations holds the stations that are chosen to be the beginning stations of the routes
        """
        super().__init__(model, score = 0)
        self.begin_stations = []
        self.load_begin_stations()
    
    def load_begin_stations(self) -> None:
        """
        Makes a list with station with one connection. Afterwards appends all the stations with amount
        of connections in ascending order to self.begin_stations. Afterwards appends the one_stations 
        to self.begin_stations. 
        """
        # collect all stations with one connnection
        one_stations = []
        for station in self.model.stations.values():
            if len(station.get_connections()) == 1:
                one_stations.append(station)
        
        # sort all other stations
        for connection_count in range(3, 10):
            for station in self.model.stations.values():
                if len(station.get_connections()) == connection_count:
                    self.begin_stations.append(station)

        # add one_stations to self.begin_stations
        for station in one_stations:
            self.begin_stations.append(station)
    
    def add_begin_option(self, train_id: int) -> None:
        """
        Adds the one begin station from self.begin_station to self.options for route with corresponding 
        train_id
        """
        print("CHOSEN")
        route = Route(train_id)
        station = self.begin_stations.pop()
        new_option = route.deep_copy_route()
        new_option.add_station(station)
        self.options.append(new_option)
