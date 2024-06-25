from algorithms.greedy import RandomGreedy
from classes.model import Model
import time
import csv

start = time.time()

# Number of iterations for each run and number of times to run
iterations_per_run = 1000
number_of_runs = 10
results = []

for run in range(number_of_runs):
    model = Model("Nederland")
    gred = RandomGreedy(model)
    best_model = gred.run(iterations_per_run)

    routes_data, score_line = best_model.get_routes_and_score()
    results.append(routes_data + [score_line])

end = time.time()

# Save results to CSV
with open('best_models.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(['route', 'stations'])
    for result in results:
        for line in result:
            writer.writerow(line.split(','))  # Split the line by comma to avoid enclosing train_id in quotes
        writer.writerow([])  # Add an empty row after each model's data

print(f'Runtime: {end - start}')
