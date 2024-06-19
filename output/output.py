from classes.model import Model
import csv

def output(model: Model):
    """
    This function generates an output file in csv format.
    It takes values from a model

    """

    # Initiate data list of lists with a header
    data = [['train', 'stations']]


    # get all routes from the model
    id_counter = 1
    for route in model.routes.values():
        stations = [station.name for station in route.stations]
        # Format the list to omit quotation marks
        stations_str = f"[{', '.join(stations)}]"
        data.append([f'train_{id_counter}', stations_str])
        id_counter += 1


    # footer of the table contains the score of the model
    data.append(['score', model.calculate_score()])

    # write data to CSV file
    filename = "output/model_output.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Data has been written to {filename}")


