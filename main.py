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
parser.add_argument('-cov', '--depthfcov', help="Uses the depth first but gets more coverage.", action="store_true")
parser.add_argument('-r', '--random', help="Uses the random algorithm.", action="store_true")

#choose experiment.
parser.add_argument('-dfexp', '--dfexperiments', help="Provides one of the pre made experiments for the depth first algorithm.",nargs='?', default=1, type=int, choices=[1,2,3,4,5,6,7,8])

#choose the iteration amount.
parser.add_argument('iteration', help='amount of iterations used for the chosen algorithm', nargs='?', default=1000, type=int)

args: argparse.Namespace= parser.parse_args()

if args.nederland:
    model = Model("Nederland")
    filename = "Nederland"
elif args.holland:
    model = Model("Holland")
    filename = "Holland"

iterations = args.iteration

dfexp = DF_experiment(filename)

if __name__ == "__main__":
    if args.randomgreedy:
        gred = RandomGreedy(model)
        gred.run(iterations)
    elif args.hillclimber:
        hc = HillClimber(model)
        hc.run(iterations)
    elif args.depthfcov and args.depthfall:
        cov_a = Depth_first_all(model)
        new_model = cov_a.run(True)
    elif args.depthfcov and args.depthfchosen:
        cov_c = Depth_first_chosen(model)
        new_model = cov_c.run(True)
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

    if args.dfexperiments == 1:
        dfexp.one_all_stations()
    elif args.dfexperiments == 2:
        dfexp.twice_all_stations()
    elif args.dfexperiments == 3:
        dfexp.trice_all_stations()
    elif args.dfexperiments == 4:
        dfexp.one_chosen_stations()
    elif args.dfexperiments == 5:
        dfexp.twice_chosen_stations()
    elif args.dfexperiments == 6:
        dfexp.trice_chosen_stations()
    elif args.dfexperiments == 7:
        dfexp.comb_chosen_all_stations()
    elif args.dfexperiments == 8:
        dfexp.comb_all_chosen_stations()











