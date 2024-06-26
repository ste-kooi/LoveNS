from classes.model import Model
from algorithms.randomise import *

import copy
import random


class HillClimber:
    """
    The HillClimber class that optimizes routes in the model by iteratively applying mutation methods.
    Each improvement or equivalent solution is kept for the next iteration.

    Parameters
    ----------
    model : Model
        A model that contains routes.
    method_frequencies : list[int]
        A list of four integers specifying the frequencies for each mutation method.
    """
    def __init__(self, model: Model, method_frequencies=None) -> None:
        if method_frequencies and len(method_frequencies) != 4:
            raise ValueError("method_frequencies must contain exactly four integers.")

        self.model = copy.deepcopy(model)
        self.score = model.calculate_score()
        self.method_list = self.set_method_list(method_frequencies)
        self.score_list = []

    def set_method_list(self, freq: list[int]):
        """
        Sets the method list based on specified frequencies.
        All methods are used once if no frequencies are specified.
        """
        if freq is not None:
            method_frequencies = {
                self.mutate_single_route: freq[0],
                self.mutate_end_of_routes: freq[1],
                self.delete_routes: freq[2],
                self.reorder_single_route: freq[3]
            }
        else:
            method_frequencies = {
                self.mutate_single_route: 1,
                self.mutate_end_of_routes: 1,
                self.delete_routes: 1,
                self.reorder_single_route: 1
            }

        method_list = []
        for method, frequency in method_frequencies.items():
            method_list.extend([method] * frequency)
        return method_list

    def mutate_single_route(self, new_model: Model):
        """
        Changes the stations of a random route to random stations.
        """
        if not new_model.routes:
            return
        random_route_id = random.choice(list(new_model.routes))
        random_reconfigure_route(new_model, random_route_id)

    def mutate_two_routes(self, new_model: Model):
        """
        Changes the stations of two random routes to random stations.
        """
        if len(new_model.routes) < 2:
            return
        random_route_id, rand_route_2 = random.sample(list(new_model.routes), 2)
        random_reconfigure_route(new_model, random_route_id)
        random_reconfigure_route(new_model, rand_route_2)

    def mutate_end_of_routes(self, new_model: Model):
        """
        Randomly removes some stations from the end of two routes and extends the first route.
        """
        if len(new_model.routes) < 2:
            return
        random_route_id = random.choice(list(new_model.routes))
        for _ in range(random.randint(1, 3)):
            new_model.get_route(random_route_id).remove_last_station()

        random_route_id_2 = random.choice(list(new_model.routes))
        for _ in range(random.randint(1, 3)):
            new_model.get_route(random_route_id_2).remove_last_station()

        new_model.update_used_connections()
        if new_model.get_route(random_route_id).get_stations():
            random_extend_route(new_model, random_route_id)
        else:
            start_station = new_model.stations[random.choice(new_model.get_stations_unused_connections())]
            random_single_route(new_model, start_station, random_route_id)

    def delete_routes(self, new_model: Model):
        """
        Deletes two random routes and creates a new route starting from an unused connection.
        """
        if len(new_model.routes) < 2:
            return
        route_1, route_2 = random.sample(list(new_model.routes), 2)
        new_model.remove_route(route_1)
        new_model.remove_route(route_2)
        start_station = new_model.stations[random.choice(new_model.get_stations_unused_connections())]
        random_single_route(new_model, start_station, route_1)

    def reorder_single_route(self, new_model: Model, route_id=None):
        """
        Reorders the route using only the stations already in the route.
        """
        if not new_model.routes:
            return
        if route_id is None:
            route_id = random.choice(list(new_model.routes))

        random_reorder_route(new_model, route_id)

    def check_score(self, new_model: Model):
        """
        Checks and accepts better or equivalent scoring models than the current model.
        """
        new_score = new_model.calculate_score()
        self.score_list.append(new_score)
        old_score = self.score

        if new_score >= old_score:
            self.model = new_model
            self.score = new_score

    def run(self, iterations: int, verbose=False, reorder=False):
        """
        Runs the HillClimber for a given number of iterations.

        Parameters
        ----------
        iterations : int
            The number of iterations to run the hill climber.
        verbose : bool, optional
            If True, prints the progress (default is False).
        reorder : bool, optional
            If True, reorders the routes at the end for additional optimization (default is False).
        """
        self.iterations = iterations

        for iteration in range(iterations):
            if verbose:
                print(f'Iteration {iteration}/{iterations}, current value: {self.score}')

            new_model = self.model.copy()
            method = random.choice(self.method_list)
            method(new_model)
            self.check_score(new_model)

        if reorder:
            self.reorder_routes(reorder)

    def reorder_routes(self, verbose=False):
        """
        Reorders all routes in the model for additional optimization.

        Parameters
        ----------
        verbose : bool, optional
            If True, prints the progress (default is False).
        """
        for route in self.model.routes:
            for iteration in range(500):
                if verbose:
                    print(f'Reorder route{route}: {iteration}/{500}, current value: {self.score}')

                new_model = self.model.copy()
                self.reorder_single_route(new_model, route)
                self.check_score(new_model)
