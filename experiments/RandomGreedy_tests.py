from algorithms.greedy import RandomGreedy
from classes.model import Model

import time

start = time.time()

model = Model("Nederland")
gred = RandomGreedy(model)
gred.run(10)

end = time.time()
