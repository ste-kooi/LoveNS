from classes.model import Model
import random
import copy

def random_routes(model: Model, amount):
    """
    Generates random routes for the model, ensuring each route does not exceed 120 minutes.

    Parameters
    ---------
    model: Model
        The model to run.
    amount : int
        The number of routes to create.

    """
    max_time = 120
    for route_id in range(1, amount + 1):

        # pick a random starting station
        current_station = random.choice(list(model.stations.values()))

        # add new route from that station
        model.add_route(current_station, route_id)

        # pick a station from the connections list
        while model.routes[route_id].duration < max_time:
            # get stations from connections and filter out visited stations
            possible_connections = [station for station in current_station.get_connections() 
                                    if model.get_station(station) not in model.get_route(route_id).get_stations()]
            if not possible_connections:
                break    
            
            # pick next station from the connections
            next_station = random.choice(possible_connections)
            next_connection = current_station.connections[next_station]

            # if addition of station to route takes to long, break
            if model.get_route(route_id).duration + next_connection.time > max_time:
                break

            # add station to route
            current_station = model.stations[next_station]
            model.routes[route_id].add_station(current_station)
  


