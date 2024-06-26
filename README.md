# loveNS
Repository inteded for the course Algorithms &amp; Heuristics - UvA Minor Programming - spring/summer 2024

## Case: RailNL
### Contents
- Case introduction
- How to use this repository
- Algorithms
- Experiments

### Case introduction    
**Terminology**     

- <u>Station</u>       : A specific location marked on a map by its x and y coordinates, which has connections to other stations.
- <u>Connection</u>    : A stretch of railroad that links two stations.
- <u>Route</u>         : A series of railroads connecting two or more stations, which defines the path a train will follow throughout the day.
- <u>Train routing</u> : The network of all routes.

This project focuses on generating the train routing for Holland and the Netherlands.    
For Holland, this must be achieved by connecting the 22 stations using the 28 possible connections.    
For the Netherlands, this must be achieved by connecting the 61 stations using the 89 possible connections.     

**Hard constraints**   

- The maximum number of routes allowed in the train routing for Holland and the Netherlands is 7 and 20, respectively.
- The maximum duration of a route in Holland and the Netherlands is 120 and 180 minutes, respectively.

**Soft constraints**   

- Utilize all possible connections
- Use as few routes as possible
- Minimize the total duration of the train routing

**Objective function**   
The train routing will be evaluated for quality using the following formula:     

K = p * 10000 - (T * 100 + Min)

- K is the quality
- p is the fraction of covered connections
- T is the number of routes used in the train routing
- Min is the total number of minutes used in the routes in the train routing

**Statespace**      
The state space of this case can be calculated using the following formula:   

Statespace = (C<sup>S</sup>)<sup>T</sup>

- C is number of connections per station
- S is number of stations per route
- T is number of routes per train routing

For the map size of Holland, the maximum value of C is 4, the maximum value of S is 24, and the maximum value of T is 7, resulting in a state space of approximately 1.4 * 10<sup>101</sup>.

For the map size of the Netherlands, the maximum value of C is 9, the maximum value of S is 36, and the maximum value of T is 20, resulting in a state space that is too big to calculate with our calculators.

### How to use this repository
**Requirements**   
The dependencies for this repository can be found in the '**requirements.txt**' file located in the root of the repository.   

**Directories**

- Algorithms  : Contains the scripts with the algorithms
- Classes     : Contains the scripts with the data structures for model, route, station, and connection
- Experiments : Contains the scripts for setting up experiments with the algorithms
- Output      : Contains the scripts for visual, terminal, and .csv output. Also includes a data folder with the experiment outputs
- Source      : Contains the .csv files with information about the stations and connections used in the data structure

**Algortihms and experiments**    
All algorithms and experiments can be accessed via main.py.   
To view all possible command line arguments, type **-h** or **--help** in the command line.   

To run an algorithm or experiment, it is mandatory to choose a map size. This repository supports two map sizes:

- Holland     : add **-hl** or **--holland** to the command line
- Netherlands : add **-nl** of **--nederland** to the command line

To run the algorithms and experiments, you can combine the map size argument with arguments listed under the specific algorithms and experiments below.

### Algortihms
**Random**    
<u>Consttructive algorithm</u>   
Generates random routes   
<u>Command lines</u>   

 - bla die bla
 - bla die bla

**Random Greedy**   
<u>Constructive algorithm</u>    
The RandomGreedy algorithm is designed to find the shortest time of all connections that a certain station has. This algorithm relies on a model that requires one of the two specific filenames. The algorithm's process starts with the `make_route` method, which creates a route by selecting random unused stations. This method sorts all possible connections from the current station based on time and selects the shortest connection that hasn’t been used in the route before. This loop continues until either the maximum duration for one route is reached or no other viable connections are available.

The `make_route` method is utilized within the `make_model` method. The `make_model` method loops to add routes until the maximum possible number of routes is reached. After adding each route, it checks the model's score. If the score decreases after adding a route, the method deletes that route and finalizes the model.

The `compare_score` method is used to compare the scores of two different models. If the new model has a higher score than the old model, the new model is retained.

Lastly, the `run` method executes the `make_model` method for a specified number of iterations. During each iteration, it compares the new model's score with the best model's score obtained so far. After running the specified number of iterations, it returns the best model based on the score.


<u>Command lines</u>

 - `--rg`, `--randomgreedy`: Uses the RandomGreedy algorithm.


**Depth First**<br>  
<u>Constructive algorithm</u>   
The depth-first (DF) algorithm is designed to explore route options systematically and improve the train routing solution based on the scoring function, making it suitable for optimizing train schedules within the given constraints. The DF algorithm’s systematic approach ensures that all possible routes are considered, allowing for a complete exploration of potential solutions to the train routing problem.

The DF algorithm takes the most recent route from a stack and explores its possible route options. For this route, it identifies all possible connections from the last station in the route. If the new connection has not been used in the route and the duration of the route is within the allowed limit, the new route is pushed onto the stack.

Two variants of the DF algorithm are implemented in this repository:     
**Depth first all (DFA) algorithm**     
This algorithm is designed to explore all possible starting stations for each route. It creates initial route options by iterating over all stations and adding them to the stack as beginning station if they haven't been used before.

**Depth first chosen (DFC) algorithm**   
This algorithm takes a strategic approach, by pre-selecting the starting stations. It pre-selects starting stations based on the number of connections a station holds. At first the stations with only one connection are used as a beginning station. After all stations with one connection are used, the stations with the most connections are used.

An additional feature has been added to enable users to emphasize coverage more within the DFA and DFC algorithms. This enhancement involves implementing a modified scoring function to evaluate route quality. Specifically, if a route achieves 100% coverage of all connections, it receives a bonus of 100 points. The regular score will still be displayed in the output.

<u>Bias</u>    
The DFA exhibits several biases:

- It constructs train routes one at a time, rather than considering all routes simultaneously. Because of this, it is possible that the most optimal solution will not be achieved.
- Another bias lies in the validation of new route options. The algorithm it is not allowed to use a connection more than once within a single route. Therefore, there is no guarantee that the most optimal solution will be generated.
- Both the DFA and DFC algorithms exhibit bias by potentially overlooking more optimal starting stations.

<u>Command lines</u>   

 - `**dfa**`, `**--depthfall**` : runs the depth first all stations algorithm
 - `**dfc**`, `**--depthfchosen**` : runs the depth first chosen stations algorithm
 - `**cov**`, `**--depthfcov**` : add cov to command line along with dfa or dfc to emphasise coverage

**Hill Climber**   
Iterative algorithm   
Hillclimber is an algorithm that optimizes a route by making a change to the model and keeping that change if it increases the model's k-score. Hillclimber algorithm must be initialised with a completed model. For a given number of iterations hillclimber randomly makes an adjustment. These adjustments can be: `mutate_single_route`, this deletes all stations from a route and fills the route with new stations with the `random_recondigure_route` function; `mutate_end_of_routes`, this removes 1 to 4 stations from the end of 2 routes. Then will only extend one route using `random_extend_route`. If the deletions lead to an empty route a new route is generated with `random_single_route`; `delete_routes` randomly removes 2 routes and generates a new route using `random_single_route`; `reorder_single_route`, reorders the route with `random_reorder_route`.

A normal hillclimber randomly picks between the adjustment using even ratios. The ratios can be customised by initializing a Hillclimber with a method_frequencies argument: `Hillclimber(model, methodfrequencies)` the method frequencies must be a list of 4 integers and correspont with `mutate_single_route, mutate_end_of_routes, delete_routes, `reorder_single_route` respectively. If no argument is parsed the default 1:1:1:1 ratio is used.

<u>Command lines</u>:

 - **-hc**, **--hillclimber** : runs the hillclimber algorithm
 - **iterations** : runs the hillclimber algorithm for the given iterations, default set to 1000
 - **-freq**, **--frequencies** : sets the method frequencies example usage: `-nl -hc -freq 2 1 3 1`

 Flags:
 - **-v**, **--verbose** : If verbose is called every iteration and its score is now printed.
 - **-ro**, **--reorder** : Ends a hillclimber run with randomly reordering every route 500 times and saves improvements.


### Experiments
**Baseline - random algorithm**    
bla die bla   

<u>Command lines</u>

 - bla die bla
 - bla die bla

**Depth First experiments**     
All DF experiment data can be found in output/data/df.     
The naming of the files consists of the mapsize, experiment, algorithm, iteration.    
For example experiment 2 generates: **hl\_exp2\_dfa\_first** and **hl\_exp2\_dfa\_second**

Experiments **1**, **2** and **3** are experiments with respectively one, two or three iterations of the DFA algorithm.

Experiments **4**, **5** and **6** are experiments with respectively one, two or three iterations of the DFC algorithm.

Experiment **7**, **9** and **10** run a DFC algorithm in the first iteration and a DFA in the second, using the generated model from the first iteration. Experiment 9 uses the coverage bonus on both iterations. Experiment 10 uses the coverage bonus only on the second iteration.

Experiment **8** runs a DFA algorithm in the first iteration and a DFC in the second, using the generated model from the first iteration.

Experiment **11** runs a DFC algortihm in the first iteration and a DFA algorithm with coverage bonus in the second and third iteration.

Experiment **12** runs a DFC algorithm in the first iteration and a DFA algorithm in the second and third iteration.

<u>Command lines</u>

 - `**-dfexp**` or `**--dfexperiments**`
 - In combination with the experiment `**number**`
 - For example: `**-dfexp 2**`

**Hill Climber experiments**    


<u>Command lines</u>   

 - bla die bla
 - bla die bla

