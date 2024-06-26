from algorithms.randomise import random_routes
from classes.model import Model

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random


class Baseline:

    def __init__(self, model: Model, iterations):
        """
        Baseline runs a random algortithm multiple times to extract statistics.
        Returns a probability distribution of scores from valid models


        """
        self.model = model
        self.iterations = iterations
        self.scores = []
        self.valid_model = 0

    def run(self):
        counter = 0
        # Run
        print('Running baseline')
        while counter < self.iterations:
            # set the number of tracks
            max_tracks = random.randint(self.model.max_routes - 4, self.model.max_routes)

            # Make random routes
            random_routes(self.model, max_tracks)

            # Save the score and number of valid models in holland
            if self.model.mapname == 'Holland' and self.model.get_coverage() == 1:
                self.scores.append(self.model.calculate_score())
                self.valid_model += 1
            # Save all models in nederland
            elif self.model.mapname == 'Nederland':
                self.scores.append(self.model.calculate_score())
                self.valid_model += 1

            counter += 1

            # clear the model
            self.model.clear_routes()

            # print the progress in the loop
            if counter % (self.iterations / 10) == 0:
                print(f'{counter/self.iterations*100}%')

    def plot_distribution(self):
        # Make a plot
        plt.figure(figsize=(10, 6))
        sns.histplot(self.scores, bins=50, kde=True, stat='probability')

        # Add titles
        plt.title('Probability Distribution of Solution Scores')
        plt.xlabel('Score')
        plt.ylabel('Probability')

        # Calculate and add statistics
        avg_score = np.mean(self.scores)
        min_score = np.min(self.scores)
        max_score = np.max(self.scores)
        stats_text = f'Number of models: {self.valid_model}\nBest score: {max_score}\nAverage score: {avg_score:.2f}\nWorst score: {min_score}'

        # Add the statistics text to the plot
        plt.text(0.02, 0.95, stats_text, transform=plt.gca().transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round,pad=0.5', edgecolor='gray', facecolor='white'))

        # save the plot
        plt.savefig('output/baseline_distribution.png')
