import csv
import sys
import os

# Add the path to the classes folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../classes')))
from model import Model
from test_model import test_model
from test_model import test_model_nl


def output(model: Model):
    """
    This function generates an output file in csv format.
    It takes values from a model
    
    """

    # Initiate data list of lists with a header
    data = [['train', 'stations']]

    
    # get all routes from the model
    for route in model.routes.values():
        stations = [station.name for station in route.stations]
        # Format the list to omit quotation marks
        stations_str = f"[{', '.join(stations)}]" 
        data.append([f'train_{route.train_id}', stations_str])
  

    # footer of the table contains the score of the model
    data.append(['score', model.calculate_score()])

    # write data to CSV file
    filename = "output/model_output.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Data has been written to {filename}")


if __name__ == "__main__":
    output(test_model_nl())