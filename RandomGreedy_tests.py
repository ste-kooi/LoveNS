from algorithms.greedy import RandomGreedy
from classes.model import Model
from output.output import output_multiple

import time
import math


best_outputs = 5
best_models = []
n_runs = 0

for best in range(best_outputs):
    model = Model("Nederland")
    gred = RandomGreedy(model)

    start = time.time()
    while time.time() - start < 5:
        best_model = gred.run(1)
        n_runs += 1

    best_models.append(best_model)

output_multiple(best_models, f"experiments/NL_RandomGreedy/RandomGreedy_0")

end2 = time.time()

print(f'Total time: {best_model.total_time()}')
print(f'Coverage: {best_model.get_coverage()}')
print(f'Final score: {gred.score}')
print(f'Runtime: {end2 - start}')
print(f'States: {gred.states}')
print(f'Iterations used: {gred.iteration_count * best_outputs}')




