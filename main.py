from algorithms.greedy import RandomGreedy
from algorithms.greedy import RandomGreedy
from algorithms.randomise import random_routes
from algorithms.Hillclimber import HillClimber
from algorithms.depth_first import Depth_first_all, Depth_first_chosen

from classes.model import Model
from experiments.depth_first_experiments import DF_experiment
from experiments.method_ratio import HillclimberMethodFrequencies
from experiments.baseline import Baseline

from output.output import output
from output.visualisation import visualise
import pandas
import argparse

def main():
    print(pandas.__version__)
    parser = argparse.ArgumentParser()

    # choose which spectrum the algortihms should work on.
    parser.add_argument('-nl', '--nederland', help= 'uses Nederland for the algorithms', action='store_true')
    parser.add_argument('-hl', '--holland', help= 'uses Holland for the algorithms', action='store_true')

    # choose which algorithm to run.
    parser.add_argument('-rg', '--randomgreedy', help="Uses the RandomGreedy algorithm.", action='store_true')
    parser.add_argument('-hc', '--hillclimber', help="Uses the HillClimber algorithm.", action='store_true')
    parser.add_argument('-dfa', '--depthfall', help="Uses the depth first all algorithm.", action="store_true")
    parser.add_argument('-dfc', '--depthfchosen', help="Uses the depth first chosen algorithm.", action="store_true")
    parser.add_argument('-cov', '--depthfcov', help="Uses the depth first but gets more coverage.", action="store_true")
    parser.add_argument('-r', '--random', help="Uses the random algorithm.", action="store_true")

    #choose experiment.
    parser.add_argument('-dfexp', '--dfexperiments', help="Provides one of the pre made experiments for the depth first algorithm.",nargs='?', default=0, type=int, choices=[1,2,3,4,5,6,7,8,9,10,11,12])
    parser.add_argument('-hmf', '--hcmethodfreq', help='Runs hillclimbers with unique mix of method frequencies', nargs=2, metavar=('iterations', 'amount'), type=int)
    parser.add_argument('-bl', '--baseline', help='Runs a baseline for a model, plotting the scores of the generated models', nargs=1, metavar=('iterations'), type=int)

    # choose the number of iterations.
    parser.add_argument('iteration', help='amount of iterations used for the chosen algorithm', nargs='?', default=1000, type=int)

    # verbose and reorder flags
    parser.add_argument('-v', '--verbose', help='Turns on printing of hillclimber iterations', action='store_true')
    parser.add_argument('-ro', '--reorder', help='Reorders every route 500 times at end of hillclimber', action='store_true')

    # Argument for frequencies list
    parser.add_argument('-freq', '--frequencies', help='List of 4 integers for hillclimber method frequencies', nargs=4, type=int, metavar=('msr', 'mer', 'dr', 'rsr'))

    args: argparse.Namespace= parser.parse_args()

    if args.nederland:
        model = Model("Nederland")
        filename = "Nederland"
    elif args.holland:
        model = Model("Holland")
        filename = "Holland"
    else:
        print('Error: please specify either --holland or -- nederland.')

    iterations = args.iteration

    dfexp = DF_experiment(filename)


    if args.randomgreedy:
        gred = RandomGreedy(model)
        gred.run(iterations)
    elif args.hillclimber:
        # check flags
        verbose = True if args.verbose else False
        reorder = True if args.reorder else False
        if args.frequencies:
            freq = args.frequencies
        else:
            [1,1,1,1]

        random_routes(model, model.max_routes)

        print('Setting up hillclimber...')
        hc = HillClimber(model, freq)
        print(f'Running hillclimber {iterations} times')
        hc.run(iterations, verbose=verbose, reorder=reorder)

        output(hc.model, 'output/model_output')
        visualise(hc.model, 'output/model_fig')

    elif args.depthfcov and args.depthfall:
        cov_a = Depth_first_all(model)
        new_model = cov_a.run(True)
    elif args.depthfcov and args.depthfchosen:
        cov_c = Depth_first_chosen(model)
        new_model = cov_c.run(True)
    elif args.depthfall:
        dfa = Depth_first_all(model)
        new_model = dfa.run()
    elif args.baseline:
        bl = Baseline(model, iterations)
        bl.run()
        bl.plot_distribution()
    elif args.depthfchosen:
        dfc = Depth_first_chosen(model)
        new_model = dfc.run()
    elif args.random:
        rndm = random_routes(model, model.max_routes)
        rndm_score = model.calculate_score()
        print(model.routes)
        print(rndm_score)

    if args.dfexperiments:
        run_df_experiment(dfexp, args.dfexperiments)

    if args.hcmethodfreq:
        hmf_iterations, hmf_amount = args.hcmethodfreq
        hmf = HillclimberMethodFrequencies(model)
        hmf.run(hmf_iterations, hmf_amount)

def run_df_experiment(dfexp, experiment_number):
    if experiment_number == 1:
        dfexp.df_experiment1()
    elif experiment_number == 2:
        dfexp.df_experiment2()
    elif experiment_number == 3:
        dfexp.df_experiment3()
    elif experiment_number == 4:
        dfexp.df_experiment4()
    elif experiment_number == 5:
        dfexp.df_experiment5()
    elif experiment_number == 6:
        dfexp.df_experiment6()
    elif experiment_number == 7:
        dfexp.df_experiment7()
    elif experiment_number == 8:
        dfexp.df_experiment8()
    elif experiment_number == 9:
        dfexp.df_experiment9()
    elif experiment_number == 10:
        dfexp.df_experiment10()
    elif experiment_number == 11:
        dfexp.df_experiment11()
    elif experiment_number == 12:
        dfexp.df_experiment12()


if __name__ == '__main__':
    main()



