from algorithms.greedy import RandomGreedy
from classes.model import Model
from output.output import output_multiple

import time

start = time.time()
best_outputs = 3
best_models = []

for best in range(best_outputs):
    model = Model("Nederland")
    gred = RandomGreedy(model)
    best_model = gred.run(1000)
    best_models.append(best_model)

output_multiple(best_models, f"experiments/RandomGreedy_0")

end = time.time()

print(f'Total time: {best_model.total_time()}')
print(f'Coverage: {best_model.get_coverage()}')
print(f'Final score: {gred.score}')
print(f'Runtime: {end - start}')
print(f'States: {gred.states}')
print(f'Iterations used: {gred.iteration_count}')


