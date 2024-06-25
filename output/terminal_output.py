from classes.model import Model

def missed_connections(model: Model):
    all_connections = set(model.connections.keys())
    for route in model.routes.values():
        for interconnection in route.interconnections:
            connection_id = interconnection.get_id()
            if connection_id in all_connections:
                all_connections.remove(connection_id)
    # print(all_connections)
    if all_connections:
        print("Missed connections:")
        for connection in all_connections:
            print(f" * {model.connections[connection]}")
        print()

def interim_overview(model, train_id):
    print(f"Route {train_id} finished")
    print(f" - Calculate_score()  : {model.calculate_score()}")
    print(f" - Coverage           : {model.get_coverage()}")
    print(f" - Route duration     : {model.routes[train_id].duration}")
    print(f" - Amount of stations : {len(model.routes[train_id].stations)}")
    print()
    
def total_overview(model, states, start = 0, end = 0):
    print("TOTAL OVERVIEW")
    print(f" - Calculate_score()   : {model.calculate_score()}")
    print(f" - Coverage            : {model.get_coverage()}")
    print(f" - Amout routes        : {len(model.routes)}")
    print(f" - Total time          : {model.total_time()} min")
    print(f" - States / iterations : {states}")
    if start != 0:
        print(f" - Running time        : {end - start}")
    print()
            