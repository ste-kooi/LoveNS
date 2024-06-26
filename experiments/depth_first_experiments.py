from classes.model import Model
from algorithms.depth_first import Depth_first_all as DF_all
from algorithms.depth_first import Depth_first_chosen as DF_chosen
from output.output import output
from output.visualisation import visualise

class DF_experiment:
    def __init__(self, mapname: str):
        self.model = Model(mapname)
        if self.model == "Holland":
            self.name = "hl"
        else:
            self.name = "nl"
    
    def df_experiment1(self):
        """
        Runs the dfa algorithm one time
        
        """
        one_all_alg = DF_all(self.model)
        one_all_model = one_all_alg.run()
        
        output(one_all_model, f"output/data/df/{self.name}_exp1_dfa")
        
        visualise(one_all_model, f"output/data/df/{self.name}_exp1_dfa")
    
    def df_experiment2(self):
        """
        runs the dfa algorithm two times
        """
        first_all_alg = DF_all(self.model)
        first_all_model = first_all_alg.run()
        
        second_all_alg = DF_all(first_all_model)
        second_all_model = second_all_alg.run()
        
        output(first_all_model, f"output/data/df/{self.name}_exp2_dfa_first")
        output(second_all_model, f"output/data/df/{self.name}_exp2_dfa_second")
        
        visualise(first_all_model, f"output/data/df/{self.name}_exp2_dfa_first")
        visualise(second_all_model, f"output/data/df/{self.name}_exp2_dfa_second")
    
    def df_experiment3(self):
        """
        runs the dfa algorithm three times
        """
        first_all_alg = DF_all(self.model)
        first_all_model = first_all_alg.run()
        
        second_all_alg = DF_all(first_all_model)
        second_all_model = second_all_alg.run()
        
        third_all_alg = DF_all(second_all_model)
        third_all_model = third_all_alg.run()
        
        output(first_all_model, f"output/data/df/{self.name}_exp3_dfa_first")
        output(second_all_model, f"output/data/df/{self.name}_exp3_dfa_second")
        output(third_all_model, f"output/data/df/{self.name}_exp3_dfa_thrid")
        
        visualise(first_all_model, f"output/data/df/{self.name}_exp3_dfa_first")
        visualise(second_all_model, f"output/data/df/{self.name}_exp3_dfa_second")
        visualise(third_all_model, f"output/data/df/{self.name}_exp3_dfa_thrid")
    
    def df_experiment4(self):
        """
        Runs the dfc algorithm one time
        """
        one_chosen_alg = DF_chosen(self.model)
        one_chosen_model = one_chosen_alg.run()

        output(one_chosen_model, f"output/data/df/{self.name}_exp4_dfc")
        
        visualise(one_chosen_model, f"output/data/df/{self.name}_exp4_dfc")
    
    def df_experiment5(self):
        """
        Runs the dfc algorithm two times
        """
        first_chosen_alg = DF_chosen(self.model)
        first_chosen_model = first_chosen_alg.run()
        
        second_chosen_alg = DF_all(first_chosen_model)
        second_chosen_model = second_chosen_alg.run()
        
        output(first_chosen_model, f"output/data/df/{self.name}_exp5_dfc_first")
        output(second_chosen_model, f"output/data/df/{self.name}_exp5_dfc_second")
        
        visualise(first_chosen_model, f"output/data/df/{self.name}_exp5_dfc_first")
        visualise(second_chosen_model, f"output/data/df/{self.name}_exp5_dfc_second")
        
    def df_experiment6(self):
        """
        Runs the dfc algorithm three times
        """
        first_chosen_alg = DF_chosen(self.model)
        first_chosen_model = first_chosen_alg.run()
        
        second_chosen_alg = DF_all(first_chosen_model)
        second_chosen_model = second_chosen_alg.run()
        
        third_chosen_alg = DF_all(second_chosen_model)
        third_chosen_model = third_chosen_alg.run()
        
        output(first_chosen_model, f"output/data/df/{self.name}_exp6_dfc_first")
        output(second_chosen_model, f"output/data/df/{self.name}_exp6_dfc_second")
        output(third_chosen_model, f"output/data/df/{self.name}_exp6_dfc_third")
        
        visualise(first_chosen_model, f"output/data/df/{self.name}_exp6_dfc_first")
        visualise(second_chosen_model, f"output/data/df/{self.name}_exp6_dfc_second")
        visualise(third_chosen_model, f"output/data/df/{self.name}_exp6_dfc_third")
        
    def df_experiment7(self):
        """
        Runs the dfc algorithm the first iteration
        Runs the dfa algorithm the second iteration
        """
        first_chosen_alg = DF_chosen(self.model)
        first_chosen_model = first_chosen_alg.run()
        
        second_all_alg = DF_all(first_chosen_model)
        second_all_model = second_all_alg.run()
        
        output(first_chosen_model, f"output/data/df/{self.name}_exp7_dfc_first")
        output(second_all_model, f"output/data/df/{self.name}_exp7_dfa_second")
        
        visualise(first_chosen_model, f"output/data/df/{self.name}_exp7_dfc_first")
        visualise(second_all_model, f"output/data/df/{self.name}_exp7_dfa_second")
    
    def df_experiment8(self):
        """
        Runs the dfa algorithm the first iteration
        Runs the dfc algorithm the second iteration
        """
        first_all_alg = DF_all(self.model)
        first_all_model = first_all_alg.run()
        
        second_chosen_alg = DF_chosen(first_all_model)
        second_chosen_model = second_chosen_alg.run()
        
        output(first_all_model, f"output/data/df/{self.name}_exp8_dfa_first")
        output(second_chosen_model, f"output/data/df/{self.name}_exp8_dfc_second")
        
        visualise(first_all_model, f"output/data/df/{self.name}_exp8_dfa_first")
        visualise(second_chosen_model, f"output/data/df/{self.name}_exp8_dfc_second")
        
    def df_experiment9(self):
        """
        Runs the dfc algorithm the first iteration, with coverage bonus
        Runs the dfa algorithm the second iteration, with coverage bonus
        """
        first_chosen_alg = DF_chosen(self.model)
        first_chosen_model = first_chosen_alg.run(True)
        
        second_all_alg = DF_all(first_chosen_model)
        second_all_model = second_all_alg.run(True)
        
        output(first_chosen_model, f"output/data/df/{self.name}_exp9_dfc_cov_first")
        output(second_all_model, f"output/data/df/{self.name}_exp9_dfa_cov_second")
        
        visualise(first_chosen_model, f"output/data/df/{self.name}_exp9_dfc_cov_first")
        visualise(second_all_model, f"output/data/df/{self.name}_exp9_dfa_cov_second")
        
    def df_experiment10(self):
        """
        Runs the dfc algorithm the first iteration
        Runs the dfa algorithm the second iteration, with coverage bonus
        """
        first_chosen_alg = DF_chosen(self.model)
        first_chosen_model = first_chosen_alg.run()
        
        second_all_alg = DF_all(first_chosen_model)
        second_all_model = second_all_alg.run(True)
        
        output(first_chosen_model, f"output/data/df/{self.name}_exp10_dfc_first")
        output(second_all_model, f"output/data/df/{self.name}_exp10_dfa_cov_second")
        
        visualise(first_chosen_model, f"output/data/df/{self.name}_exp10_dfc_first")
        visualise(second_all_model, f"output/data/df/{self.name}_exp10_dfa_cov_second")
        
    def df_experiment11(self):
        """
        Runs the dfc algorithm the first iteration
        Runs the dfa algorithm the second iteration, with coverage bonus
        Runs the dfa algorithm the third iteration, with coverage bonus
        """
        first_chosen_alg = DF_chosen(self.model)
        first_chosen_model = first_chosen_alg.run()
        
        second_all_alg = DF_all(first_chosen_model)
        second_all_model = second_all_alg.run(True)
        
        third_all_alg = DF_all(second_all_model)
        third_all_model = third_all_alg.run(True)
        
        output(first_chosen_model, f"output/data/df/{self.name}_exp11_dfc_first")
        output(second_all_model, f"output/data/df/{self.name}_exp11_dfa_cov_second")
        output(third_all_model, f"output/data/df/{self.name}_exp11_dfa_cov_third")
        
        visualise(first_chosen_model, f"output/data/df/{self.name}_exp11_dfc_first")
        visualise(second_all_model, f"output/data/df/{self.name}_exp11_dfa_cov_second")
        visualise(third_all_model, f"output/data/df/{self.name}_exp11_dfa_cov_third")
    
    def df_experiment12(self):
        """
        Runs the dfc algorithm the first iteration
        Runs the dfa algorithm the second iteration
        Runs the dfa algorithm the third iteration
        """
        first_chosen_alg = DF_chosen(self.model)
        first_chosen_model = first_chosen_alg.run()
        
        second_all_alg = DF_all(first_chosen_model)
        second_all_model = second_all_alg.run()
        
        third_all_alg = DF_all(second_all_model)
        third_all_model = third_all_alg.run()
        
        output(first_chosen_model, f"output/data/df/{self.name}_exp12_dfc_first")
        output(second_all_model, f"output/data/df/{self.name}_exp12_dfa_second")
        output(third_all_model, f"output/data/df/{self.name}_exp12_dfa_third")
        
        visualise(first_chosen_model, f"output/data/df/{self.name}_exp12_dfc_first")
        visualise(second_all_model, f"output/data/df/{self.name}_exp12_dfa_second")
        visualise(third_all_model, f"output/data/df/{self.name}_exp12_dfa_third")
