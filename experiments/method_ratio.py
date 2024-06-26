from classes.model import Model
from algorithms.randomise import random_routes
from algorithms.Hillclimber import HillClimber
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy
import random


class HillclimberMethodFrequencies:
    """
    This class runs multiple hillclimber algorithms with different frequencies
    of the methods the hillclimber can choose from.
    """

    def __init__(self, model: Model) -> None:
        """
        Initializes the HillclimberMethodFrequencies class.

        Parameters:
            model (Model): The empty model to be optimized by the hillclimber.
        """
        self.model = copy.deepcopy(model)
        self.iterations = 0
        self.amount = 0

    def generate_frequencies(self) -> list[int]:
        """
        Generates a list of method frequencies for the hillclimber.

        Returns:
            list[int]: Frequencies for mutate single route, mutate end of routes,
                       delete routes, and reorder single route, respectively.
        """
        msr = random.randint(0, 6)
        mer = random.randint(0, 6)
        dr = random.randint(0, 6)
        rsr = random.randint(0, 6)

        frequencies = [msr, mer, dr, rsr]
        return frequencies

    def hillclimber(self, model: Model):
        """
        Runs a hillclimber for a specific number of iterations.

        Arguments:
            model (Model): The model to be optimized.

        Returns:
            tuple: A tuple containing the score list, method frequencies,
                   and the highest scoring model.
        """
        frequencies = self.generate_frequencies()

        print("Setting up Hill Climber...")
        climber = HillClimber(model, frequencies)

        print("Running Hill Climber...")
        climber.run(self.iterations)
        return climber.score_list, frequencies, climber.model

    def plot_results(self, score_data: list[list[int]], freq_data: list[list[int]], file_name: str) -> None:
        """
        Plots the results of the hillclimber runs.

        Arguments:
            score_data (list[list[int]]):   Scores of each iteration for each run.
            freq_data (list[list[int]]):    Frequencies used in each hillclimber run.
        """
        sample_rate = 1000  # Plot every 1000th point to reduce density
        window_size = 5000  # Window size for rolling average

        plt.figure(figsize=(12, 6))

        for i, (scores, freqs) in enumerate(zip(score_data, freq_data)):
            sampled_scores = scores[::sample_rate]
            sampled_iterations = np.arange(0, self.iterations, sample_rate)
            rolling_scores = pd.Series(sampled_scores).rolling(window=window_size, min_periods=1).mean()
            plt.plot(sampled_iterations, rolling_scores, label=f'Run {i+1} (Freq: {freqs})', alpha=0.8, linewidth=1)

        plt.xlabel('Iterations')
        plt.ylabel('Score')
        plt.title('Hillclimber Score Comparison')
        plt.legend()
        plt.grid(True)

        plt.savefig(f'experiments/data/{file_name}.png')
        print(f"Figure has been saved to experiments/data/{file_name}.png")

    def plot_selected_models(self, score_data: list[list[int]], freq_data: list[list[int]], model_data: list[Model], file_name: str) -> None:
        """
        Plots the results of selected hillclimber runs, including the 3 best, worst,
        and a sample of middle-performing runs.

        Arguments:
            score_data (list[list[int]]):   Scores of each iteration for each run.
            freq_data (list[list[int]]):    Frequencies used in each hillclimber run.
            model_data (list[Model]):       Models generated by each hillclimber run.
        """
        final_scores = [model.calculate_score() for model in model_data]
        sorted_indices = np.argsort(final_scores)

        best_index = sorted_indices[-1]
        best_index_1 = sorted_indices[-2]
        best_index_2 = sorted_indices[-3]
        worst_index = sorted_indices[0]

        middle_indices = sorted_indices[1:-1]
        random_indices = random.sample(list(middle_indices), 6)

        selected_indices = [worst_index] + random_indices + [best_index_2, best_index_1, best_index]

        sample_rate = 1000
        window_size = 5000

        plt.figure(figsize=(12, 6))

        for i, idx in enumerate(selected_indices):
            scores = score_data[idx]
            freqs = freq_data[idx]
            sampled_scores = scores[::sample_rate]
            sampled_iterations = np.arange(0, self.iterations, sample_rate)
            rolling_scores = pd.Series(sampled_scores).rolling(window=window_size, min_periods=1).mean()
            plt.plot(sampled_iterations, rolling_scores, label=f'HC {i+1} (Freq: {freqs})', alpha=0.8, linewidth=1)

        plt.xlabel('Iterations')
        plt.ylabel('Score')
        plt.title(f'Hillclimber Score Comparison (selection from {len(model_data)} hillclimbers)')
        plt.legend()
        plt.grid(True)

        plt.savefig(f'experiments/data/{file_name}.png')
        print(f"Figure has been saved to experiments/data/{file_name}.png")


    def run(self, iterations: int, amount: int) -> None:
        """
        Runs a given number of hillclimbers for a specific number of iterations.
        If the hillclimbers are finished data is stored to a csv file and the figure is saved

        Arguments:
            iterations (int):   Number of iterations for each hillclimber run.
            amount (int):       Number of hillclimber runs to perform.
        """
        self.iterations = iterations
        self.amount = amount
        score_data = []
        freq_data = []
        model_data = []

        # fill the model with routes
        random_routes(self.model, self.model.max_routes)

        for i in range(self.amount):
            model_copy = copy.deepcopy(self.model)
            scores, frequencies, hc_model = self.hillclimber(model_copy)
            score_data.append(scores)
            freq_data.append(frequencies)
            model_data.append(copy.deepcopy(hc_model))

        # plot and save data
        file_name = str(input('Enter file name: '))
        if amount > 10:
            self.plot_selected_models(score_data, freq_data, model_data, file_name)
        else:
            self.plot_results(score_data, freq_data, file_name)
