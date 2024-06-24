from classes.model import Model
import random
import copy
from typing import Set

class RandomGreedy:
    """
    The greedy class creates routes using the shortest
    connection times possible for every station.
    """

    def __init__(self, model: Model) -> None:
        self.model: Model = copy.deepcopy(model)
        self.score: int = self.model.calculate_score()
        self.best_model: Model = copy.deepcopy(self.model)
        self.route_id: int = 0

    def make_route(self, new_model: Model, used_starting_stations: Set[str]) -> None:
        """
        Makes a route using the shortest connection times possible for every station.
        """
        self.route_id = len(new_model.routes) + 1
        used_connections: Set = set()
        available_stations = [station for station in new_model.stations.values() if station.name not in used_starting_stations]

        if not available_stations:
            return

        new_station = random.choice(available_stations)
        used_starting_stations.add(new_station.name)

        new_model.add_route(new_station, self.route_id)

        while new_model.routes[self.route_id].duration < new_model.max_time:
            sorted_connections = sorted(new_station.connections.values(), key=lambda con: con.time)
            best_connection = None

            for connection in sorted_connections:
                if connection not in used_connections:
                    best_connection = connection
                    break

            if not best_connection:
                break

            if best_connection.station1 == new_station:
                new_station = best_connection.station2
            else:
                new_station = best_connection.station1

            used_connections.add(best_connection)
            new_model.routes[self.route_id].add_station(new_station)
            new_model.routes[self.route_id].refresh_duration()

            if new_model.routes[self.route_id].duration >= new_model.max_time:
                new_model.routes[self.route_id].remove_last_station()
                break

    def make_models(self, new_model: Model) -> None:
        """
        Makes routes using the shortest connection times possible, ensuring each route starts from a different station.
        """
        used_starting_stations: Set[str] = set()
        best_score: int = 0
        for _ in range(self.model.max_routes):
            self.make_route(new_model, used_starting_stations)
            current_score = new_model.calculate_score()

            if current_score > best_score:
                best_score = current_score
            elif current_score < best_score:
                new_model.remove_route(self.route_id)
                break

    def compare_score(self, new_model: Model) -> None:
        """
        Compares the overall scores of 2 different models and saves the best score.
        """
        new_score = new_model.calculate_score()

        if new_score > self.score:
            print("New model has a better score. Updating the model.")
            self.best_model = new_model
            self.score = new_score
        else:
            print("New model does not have a better score. Keeping the current model.")

    def run(self, iterations: int) -> Model:
        """
        Runs the greedy algorithm for x iterations.
        """
        for iteration in range(iterations):
            print(f'Iteration {iteration + 1}/{iterations}, current value: {self.score}')
            new_model = copy.deepcopy(self.model)
            self.make_models(new_model)
            self.compare_score(new_model)

        print(f'Final score: {self.score}')
        return self.best_model
