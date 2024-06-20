from classes.model import Model
import random
import copy

class Greedy():
    """
    The greedy class creates routes using the shortest
    connection times possible for every station.
    """

    def __init__(self, model: Model) -> None:
        self.model = copy.deepcopy(model)
        self.usable_connections = self.model.connections
        self.score = self.model.calculate_score()


    def make_routes(self, new_model: Model):
        """
        Makes a route using the shortest connection times possible, for every station.

        """
        self.used_starting_station = []

        for x in range(20):
            route_id = len(new_model.routes) + 1
            used_connections = set()
            new_station = random.choice(list(new_model.stations.values()))


            while new_station.name in self.used_starting_station:
                new_station = random.choice(list(new_model.stations.values()))

            self.used_starting_station.append(new_station.name)

            new_model.add_route(new_station, route_id)

            while new_model.routes[route_id].duration < new_model.max_time:
                sorted_connections = sorted(new_station.connections.values(), key=lambda con: con.time)

                best_connection = sorted_connections[0]

                for connection in sorted_connections:
                    if connection not in used_connections:
                        best_connection = connection

                if best_connection.station1 == new_station:
                    new_station = best_connection.station2
                else:
                    new_station = best_connection.station1

                used_connections.add(best_connection)
                new_model.routes[route_id].add_station(new_station)
                new_model.routes[route_id].refresh_duration()

                if new_model.routes[route_id].duration >= 120:
                    new_model.routes[route_id].remove_last_station()
                    used_connections = set()
                    break
        print(new_model.calculate_score())
        print(new_model.routes)

    def make_models(self, new_model: Model, number_of_models):
        """
        Makes models x number of models.
        """
        for _ in range(number_of_models):
            self.make_routes(new_model)

    def compare_score(self, new_model: Model):
        """
        Compares the overall scores of 2 different
        models and saves the best score.
        """
        new_score = new_model.calculate_score()
        old_score = self.score

        if new_score >= old_score:
            self.model = new_model
            self.score = new_score

    def run(self, iterations: int):
        """
        Runs the greedy class for x iterations.
        """
        for iteration in range(iterations):

            print(f'Iteration {iteration}/{iterations}, current value: {self.score}')

            # create copy of the model to simulate the change
            new_model = copy.deepcopy(self.model)

            method = random.choice([self.make_routes, self.make_models])

            # Call the selected method with the appropriate parameters
            if method == self.make_routes:
                method(new_model)
            else:
                method(new_model, number_of_models=1)

            # Compare the scores and potentially update the model
            self.compare_score(new_model)
