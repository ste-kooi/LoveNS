from .Hillclimber import HillClimber
from classes.model import Model

import random
import math


class SimulatedAnnealing(HillClimber):
    """
    The SimulatedAnnealing class that changes a random route in the graph to a random valid value.
    Each improvement or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.
    """
    def __init__(self, model: Model, temperature=1):
        # Use the init of the Hillclimber class
        super().__init__(model)

        # Starting temperature and current temperature
        self.T0 = temperature
        self.T = temperature
        self.iterations = 1

    def update_temperature(self):
        """
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """
        self.T = self.T - (self.T0 / self.iterations)

        # Exponential would look like this:
        # alpha = 0.95
        # self.T = self.T * alpha

        # where alpha can be any value below 1 but above 0

    def check_score(self, new_model: Model):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        new_score = new_model.calculate_score()
        old_value = self.score

        # Calculate the probability of accepting this new graph
        delta =  old_value - new_score


        # Define reasonable bounds for the exponent
        min_exponent = -709  # Close to the smallest value that math.exp can handle
        max_exponent = 709   # Close to the largest value that math.exp can handle

        # Calculate the exponent with clamping
        exponent = -delta / self.T
        clamped_exponent = max(min(exponent, max_exponent), min_exponent)

        # Calculate the probability
        probability = math.exp(clamped_exponent)

        # NOTE: Keep in mind that if we want to maximize the value, we use:
        # delta = old_value - new_value

        # Pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.model = new_model
            self.score = new_score

        # Update the temperature
        self.update_temperature()
