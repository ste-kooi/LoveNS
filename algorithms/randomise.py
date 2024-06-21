from classes.model import Model
import random
import copy

def random_routes(model: Model, amount):
    """
    Generates a specific amount of random routes for the model.

    Parameters
    ---------
    model: Model
        The model to run.
    amount : int
        The number of routes to create.

    """
    for route_id in range(1, amount + 1):

        # pick a random starting station
        current_station = random.choice(list(model.stations.values()))
        random_single_route(model, current_station, route_id)


def random_single_route(model: Model, current_station, route_id: int):
    """
    Generates a single random route.

    """
    # add new route from that station
    model.add_route(current_station, route_id)

    # pick a station from the connections list
    while model.routes[route_id].duration < model.max_time:
        # get stations from connections and filter out stations visited more than twice
        possible_connections = [station for station in current_station.get_connections()
                                if model.get_route(route_id).get_stations().count(model.get_station(station)) < 2]
        if not possible_connections:
            break

        # pick next station from the connections
        next_station = random.choice(possible_connections)
        next_connection = current_station.connections[next_station]

        # if addition of station to route takes to long, break
        if model.get_route(route_id).duration + next_connection.time > model.max_time:
            break

        # add station to route
        current_station = model.stations[next_station]
        model.routes[route_id].add_station(current_station)

    model.update_used_connections()


def random_reorder_route(model: Model, route_id: int):

    # Get the stations in the current route
    stations = model.get_route(route_id).get_stations()
    stat_set = set(stations)  # Set of unique stations to visit

    # Remove the current route from the model
    model.remove_route(route_id)

    # Start with the first station in the list
    if len(stations) >= 4:
        current_station = random.choice(stations[:1] + stations[-2:])
    else:
        current_station = random.choice([stations[0]] + [stations[-1]])
    model.add_route(current_station, route_id)

    visited_stations = {current_station}

    while len(visited_stations) < len(stat_set):
        # Get possible connections from the current station
        possible_connections = [station for station in current_station.get_connections()
                                if model.get_station(station) in stat_set]

        if not possible_connections:
            break

        # Pick the next station from possible connections
        next_station = random.choice(possible_connections)
        next_connection = current_station.connections[next_station]

        # Check if adding the station exceeds the max duration
        if model.get_route(route_id).duration + next_connection.time > model.max_time:
            break

        # Add the station to the route
        current_station = model.stations[next_station]
        model.routes[route_id].add_station(current_station)
        visited_stations.add(current_station)





def random_reconfigure_route(model: Model, route_id: int):
    """
    This function changes a route by deleting it and its connections from the model
    and generating a random route from a station with unused connections
    """
    # update used_connections
    model.used_connections = model.used_connections - model.routes[route_id].interconnections

    # clear route
    model.remove_route(route_id)

    # generate new random route
    current_station = model.get_station(random.choice(model.get_stations_unused_connections()))
    random_single_route(model, current_station, route_id)


def random_extend_route(model: Model, route_id):
    """
    Generates a single random route.

    """
    current_station = model.get_route(route_id).get_stations()[-1]

    # pick a station from the connections list
    while model.routes[route_id].duration < model.max_time:
        # get stations from connections and filter out stations visited more than twice
        possible_connections = [station for station in current_station.get_connections()
                                if model.get_route(route_id).get_stations().count(model.get_station(station)) < 2]
        if not possible_connections:
            break

        # pick next station from the connections
        next_station = random.choice(possible_connections)
        next_connection = current_station.connections[next_station]

        # if addition of station to route takes to long, break
        if model.get_route(route_id).duration + next_connection.time > model.max_time:
            break

        # add station to route
        current_station = model.stations[next_station]
        model.routes[route_id].add_station(current_station)
    model.update_used_connections()

    pass


def random_routes_2(model: Model, amount):
    """
    Generates random routes for the model, ensuring each route does not exceed max_time.
    No connections are used more than twice and starting stations are stations with unused connections.

    Parameters
    ---------
    amount : int
        The number of routes to create.

    -- dit gaat uiteindelijk naar algorithms --
    """
    for route_id in range(1, amount + 1):

        # Check if there are any stations with unused connections
        stations_with_unused_connections = model.get_stations_unused_connections()
        if not stations_with_unused_connections:
            break

        # pick a starting station
        current_station = model.stations[random.choice(stations_with_unused_connections)]

        # add new route from that station
        model.add_route(current_station, route_id)

        # pick a station from the connections list
        while model.routes[route_id].duration < model.max_time:
            # get stations from connections and filter out visited stations
            possible_connections = [station for station in current_station.connections
                                    if model.get_route(route_id).get_stations().count(model.get_station(station)) < 2]

            rand = random.randint(1,10)
            if rand >= 2:
                possible_connections = [station for station in possible_connections if
                                        current_station.connections[station] not in
                                        model.used_connections]
            if not possible_connections:
                break

            # pick next station from the connections
            next_station = random.choice(possible_connections)
            next_connection = current_station.connections[next_station]

            # if addition of station to route takes to long, break
            if model.routes[route_id].duration + next_connection.time > model.max_time:
                break

            # add station to route
            current_station = model.stations[next_station]
            model.routes[route_id].add_station(current_station)
                # update the used connections in a route to the model
        model.update_used_connections()







