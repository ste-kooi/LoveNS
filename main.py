from algorithms.greedy import RandomGreedy
from algorithms.randomise import random_routes
from algorithms.Hillclimber import HillClimber
from classes.model import Model

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('randomgreedy', help= 'uses the RandomGreedy algorithm', type=str)

args: argparse.Namespace= parser.parse_args()

print(args.randomgreedy)




