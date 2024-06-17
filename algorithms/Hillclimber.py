from classes.model import Model
from algorithms.randomise import random_reconfigure_route
from output.output import output
from output.visualisation import visualise


import time
import copy
import random


class HillClimber:
    """
    The HillClimber class that changes a random route in the model to random valid route. Each imporvement
    or equivalent solution is kept for the next iteration. 
    """
    def __init__(self, model: Model) -> None:
        self.model = copy.deepcopy(model)
        self.score = model.calculate_score()

    def mutate_single_route(self, new_model: Model):
        """
        Changes the stations of a random route to random stations
        """
        random_route_id = random.choice(list(new_model.routes))
        random_reconfigure_route(new_model, random_route_id)


    def mutate_model(self, new_model, number_of_routes=1):
        """
        Changes the value of a number of routes with a random valid value.
        """
        for _ in range(number_of_routes):
            self.mutate_single_route(new_model)


    def check_score(self, new_model: Model):
        """
        Checks and accepts better scoring models than the current model
        """
        new_score = new_model.calculate_score()
        old_score = self.score


        # accept higher scores
        if new_score >= old_score:
            self.model = new_model
            self.score = new_score

    def run(self, iterations: int, mutate_routes_number = 1):
        """
        Runs the HillCLimber for a given number of iterations.
        """
        for iteration in range(iterations):

            print(f'Iteration {iteration}/{iterations}, current value: {self.score}') 

            # create copy of the model to simulate the change
            new_model = copy.deepcopy(self.model)

            self.mutate_model(new_model, number_of_routes=mutate_routes_number)

        
            self.check_score(new_model)