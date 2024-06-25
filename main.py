from algorithms.greedy import RandomGreedy
from algorithms.randomise import random_routes
from classes.model import Model
from experiments.depth_first_experiments import DF_experiment

if __name__ == "__main__":
    # model = Model("Nederland")
#     gred = Greedy(model)
#     gred.run(10)
    
    # depth first experiment
    dfExperiment_hl = DF_experiment("Holland")
    dfExperiment_nl = DF_experiment("Nederland")
    
    dfExperiment_hl.one_all_stations()
    dfExperiment_hl.twice_all_stations()
    
    dfExperiment_nl.one_all_stations()
    dfExperiment_nl.twice_all_stations()

