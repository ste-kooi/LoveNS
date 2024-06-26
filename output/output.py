from classes.model import Model
import csv

def output(model: Model, file_path: str, states = 0, start = 0, end = 0):
    """
    This function generates an output file in csv format.
    It takes values from a model
    Writes output to file_path.csv

    """

    # Initiate data list of lists with a header
    data = [['train', 'stations', 'route duration']]


    # get all routes from the model
    id_counter = 1
    for route in model.routes.values():
        stations = [station.name for station in route.stations]
        # Format the list to omit quotation marks
        stations_str = f"[{', '.join(stations)}]"
        data.append([f'train_{id_counter}', stations_str, route.duration])
        id_counter += 1


    # footer of the table contains the score of the model
    data.append([])
    data.append(['score', model.calculate_score()])
    data.append(['coverage', model.get_coverage()])
    data.append(['total time', model.total_time()])
    if states > 0:
        data.append(['states', states])
    if start != 0:
        data.append(['running time', end - start])
    
    
    # write data to CSV file
    filename = f"{file_path}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Data has been written to {file_path}.csv")


def output_multiple(models: list[Model], file_path: str):
    """
    This function generates an output file in CSV format for multiple models.
    Each model's data is stacked with a blank line in between.

    Args:
    - models (list[Model]): List of Model instances to generate output for.
    - file_path (str): File path (without extension) where the output CSV will be saved.
    """
    with open(f"{file_path}.csv", mode='w', newline='') as file:
        writer = csv.writer(file)

        for index, model in enumerate(models):
            if index > 0:
                writer.writerow([])  # Add a blank line between models

            writer.writerow(['train', 'stations'])

            id_counter = 1
            for route in model.routes.values():
                stations = [station.name for station in route.stations]
                stations_str = f"[{', '.join(stations)}]"
                writer.writerow([f'train_{id_counter}', stations_str])
                id_counter += 1

            writer.writerow(['score', model.calculate_score()])

    print(f"Data has been written to {file_path}.csv")



