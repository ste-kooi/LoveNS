from algorithms.greedy import RandomGreedy
from classes.model import Model
from output.output import output_multiple
from output.visualisation import visualise

import time

def experiment()
    best_outputs = 5
    best_models = []
    iteration_total = 0
    start = time.time()

    for best in range(best_outputs):
        model = Model("Nederland")
        gred = RandomGreedy(model)

        start_gred = time.time()
        while time.time() - start_gred < 600:
            best_model = gred.run(1)
            iteration_total += 1

        best_models.append(best_model)

    output_multiple(best_models, f"experiments/NL_RandomGreedy/RandomGreedy_2")
    visualise(best_model, f"experiments/NL_RandomGreedy/RandomGreedy_img2")

    end = time.time()

    print(f'Total time: {best_model.total_time()}')
    print(f'Coverage: {best_model.get_coverage()}')
    print(f'Final score: {gred.score}')
    print(f'Runtime: {end - start}')
    print(f'States: {gred.states}')
    print(f'Iterations used: {iteration_total}')




