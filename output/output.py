from classes import Model
import csv

def output(model: Model):
    """
    This function generates an output file in csv format.
    It takes values from a model
    
    """

    # Initiate data list of lists with a header
    data = [['train', 'stations']]

    
    # get all routes from the model
    for route in model.routes:
        data.append([route.train_id, f"{route.stations}"])

    # footer of the table contains the score of the model
    data.append(['score', model.calculate()])

    # write data to CSV file
    filename = "output/model_output.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Data has been written to {filename}")
        
