from algorithms.greedy import RandomGreedy
from algorithms.greedy import RandomGreedy
from algorithms.randomise import random_routes
from algorithms.Hillclimber import HillClimber
from algorithms.depth_first import Depth_first_all, Depth_first_chosen
from classes.model import Model
from experiments.depth_first_experiments import DF_experiment

import argparse

parser = argparse.ArgumentParser()

#choose which spectrum the algortihms should work on.
parser.add_argument('-nl', '--nederland', help= 'uses Nederland for the algorithms', action='store_true')
parser.add_argument('-hl', '--holland', help= 'uses Holland for the algorithms', action='store_true')

#choose which algorithm to run.
parser.add_argument('-rg', '--randomgreedy', help="Uses the RandomGreedy algorithm.", action='store_true')
parser.add_argument('-hc', '--hillclimber', help="Uses the HillClimber algorithm.", action='store_true')
parser.add_argument('-dfa', '--depthfall', help="Uses the depth first all algorithm.", action="store_true")
parser.add_argument('-dfc', '--depthfchosen', help="Uses the depth first chosen algorithm.", action="store_true")
parser.add_argument('-r', '--random', help="Uses the random algorithm.", action="store_true")

#choose experiment.
parser.add_argument()
#choose the iteration amount.
parser.add_argument('iteration', help='amount of iterations used for the chosen algorithm', nargs='?', default=1000, type=int)

args: argparse.Namespace= parser.parse_args()

if args.nederland:
    model = Model("Nederland")
elif args.holland:
    model = Model("Holland")

iterations = args.iteration

if __name__ == "__main__":
    if args.randomgreedy:
        gred = RandomGreedy(model)
        gred.run(iterations)
    elif args.hillclimber:
        hc = HillClimber(model)
        hc.run(iterations)
    elif args.depthfall:
        dfa = Depth_first_all(model)
        new_model = dfa.run()
    elif args.depthfchosen:
        dfc = Depth_first_chosen(model)
        new_model = dfc.run()
    elif args.random:
        rndm = random_routes(model, model.max_routes)
        rndm_score = model.calculate_score()
        print(model.routes)
        print(rndm_score)








