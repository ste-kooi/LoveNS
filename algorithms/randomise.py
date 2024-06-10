import sys
import os
import random

# Add the path to the classes folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../classes')))
from model import Model

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../output')))
from output import output
from visualisation import visualise



def random_routes(model, amount):
    """
    Generates random routes for the model, ensuring each route does not exceed 120 minutes.

    Parameters
    ---------
    amount : int
        The number of routes to create.

    -- dit gaat uiteindelijk naar algorithms --
    """
    for train_id in range(1, amount + 1):

        # pick random starting station
        current_station = model.stations[random.choice(list(model.stations))]

        # add new route from that station
        model.add_route(current_station, train_id)

        # pick a station from the connections list
        while model.routes[train_id].duration < 120:
            # get stations from connections and filter out visited stations
            possible_connections = [station for station in current_station.connections 
                                    if model.stations[station] not in model.routes[train_id].stations]
            if not possible_connections:
                break    
            
            # pick next station from the connections
            next_station = random.choice(possible_connections)
            next_connection = current_station.connections[next_station]

            # if addition of station to route takes to long, break
            if model.routes[train_id].duration + next_connection.time > 120:
                break

            # add station to route
            current_station = model.stations[next_station]
            model.routes[train_id].add_station(current_station)
if __name__ == '__main__':
    model = Model('Holland')
    random_routes(model, 7)
    output(model)
    visualise(model)