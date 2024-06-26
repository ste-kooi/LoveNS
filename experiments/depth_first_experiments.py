from classes.model import Model
from algorithms.depth_first import Depth_first_all as DF_all
from algorithms.depth_first import Depth_first_chosen as DF_chosen
from output.output import output
from output.visualisation import visualise

class DF_experiment:
    def __init__(self, mapname: str):
        self.model = Model(mapname)
    
    def one_all_stations(self):
        one_all_alg = DF_all(self.model)
        one_all_model = one_all_alg.run()
        
        output(one_all_model, "output/data/df/df_1iter_all", one_all_alg.states, one_all_alg.start, one_all_alg.end)
        
        visualise(one_all_model, "output/data/df/df_1iter_all")
    
    def twice_all_stations(self):
        first_all_alg = DF_all(self.model)
        first_all_model = first_all_alg.run()
        
        second_all_alg = DF_all(first_all_model)
        second_all_model = second_all_alg.run()
        
        output(first_all_model, "output/data/df/df_first_2iter_all", first_all_alg.states, first_all_alg.start, first_all_alg.end)
        output(second_all_model, "output/data/df/df_second_2iter_all", second_all_alg.states, second_all_alg.start, second_all_alg.end)
        
        visualise(first_all_model, "output/data/df/df_first_2iter_all")
        visualise(second_all_model, "output/data/df/df_second_2iter_all")
    
    def trice_all_stations(self):
        first_all_alg = DF_all(self.model)
        first_all_model = twice_all_alg.run()
        
        second_all_alg = DF_all(first_all_model)
        second_all_model = second_all_alg.run()
        
        third_all_alg = DF_all(second_all_model)
        third_all_model = third_all_alg.run()
        
        output(first_all_model, "output/data/df/df_first_3iter_all", first_all_alg.states, first_all_alg.start, first_all_alg.end)
        output(second_all_model, "output/data/df/df_second_3iter_all", second_all_alg.states, second_all_alg.start, second_all_alg.end)
        output(third_all_model, "output/data/df/df_third_3iter_all", third_all_alg.states, third_all_alg.start, third_all_alg.end)
        
        visualise(first_all_model, "output/data/df/df_first_3iter_all")
        visualise(second_all_model, "output/data/df/df_second_3iter_all")
        visualise(third_all_model, "output/data/df/df_third_3iter_all")
    
    def one_chosen_stations(self):
        one_chosen_alg = DF_chosen(self.model)
        one_chosen_model = one_chosen_alg.run()

        output(one_chosen_model, "output/data/df/df_1iter_chosen", one_chosen_alg.states, one_chosen_alg.start, one_chosen_alg.end)
        
        visualise(one_chosen_model, "output/data/df/df_1iter_chosen")
    
    def twice_chosen_stations(self):
        first_chosen_alg = DF_chosen(self.model)
        first_chosen_model = first_chosen_alg.run()
        
        second_chosen_alg = DF_all(first_chosen_model)
        second_chosen_model = second_chosen_alg.run()
        
        output(first_chosen_model, "output/data/df/df_first_2iter_chosen", first_chosen_alg.states, first_chosen_alg.start, first_chosen_alg.end)
        output(second_chosen_model, "output/data/df/df_second_2iter_chosen", second_chosen_alg.states, second_chosen_alg.start, second_chosen_alg.end)
        
        visualise(first_chosen_model, "output/data/df/df_first_2iter_chosen")
        visualise(second_chosen_model, "output/data/df/df_second_2iter_chosen")
        
    def trice_chosen_stations(self):
        first_chosen_alg = DF_chosen(self.model)
        first_chosen_model = first_chosen_alg.run()
        
        second_chosen_alg = DF_all(first_chosen_model)
        second_chosen_model = second_chosen_alg.run()
        
        third_chosen_alg = DF_all(second_chosen_model)
        third_chosen_model = third_chosen_alg.run()
        
        output(first_chosen_model, "output/data/df/df_first_2iter_chosen", first_chosen_alg.states, first_chosen_alg.start, first_chosen_alg.end)
        output(second_chosen_model, "output/data/df/df_second_2iter_chosen", second_chosen_alg.states, second_chosen_alg.start, second_chosen_alg.end)
        output(third_chosen_model, "output/data/df/df_third_3iter_chosen", third_chosen_alg.states, third_chosen_alg.start, third_chosen_alg.end)
        
        visualise(first_chosen_model, "output/data/df/df_first_2iter_chosen")
        visualise(second_chosen_model, "output/data/df/df_second_2iter_chosen")
        visualise(third_chosen_model, "output/data/df/df_third_3iter_chosen")
        
    def comb_chosen_all_stations(self):
        first_chosen_alg = DF_chosen(self.model)
        first_chosen_model = first_chosen_alg.run()
        
        second_all_alg = DF_all(first_chosen_model)
        second_all_model = second_all_alg.run()
        
        output(first_chosen_model, "output/data/df/df_first_chosen_all", first_chosen_alg.states, first_chosen_alg.start, first_chosen_alg.end)
        output(second_all_model, "output/data/df/df_second_chosen_all", second_all_alg.states, second_all_alg.start, second_all_alg.end)
        
        visualise(first_chosen_model, "output/data/df/df_first_chosen_all")
        visualise(second_all_model, "output/data/df/df_second_chosen_all")
    
    def comb_all_chosen_stations(self):
        first_chosen_alg = DF_chosen(self.model)
        first_chosen_model = first_chosen_alg.run()
        
        second_all_alg = DF_all(first_chosen_model)
        second_all_model = second_all_alg.run()
        
        output(first_chosen_model, "output/data/df/df_first_chosen_all", first_chosen_alg.states, first_chosen_alg.start, first_chosen_alg.end)
        output(second_all_model, "output/data/df/df_second_chosen_all", second_all_alg.states, second_all_alg.start, second_all_alg.end)
        
        visualise(first_chosen_model, "output/data/df/df_first_chosen_all")
        visualise(second_all_model, "output/data/df/df_second_chosen_all")
        
        
