import sys
import os
import matplotlib.pyplot as plt
from itertools import cycle

# Add the path to the classes folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../classes')))
from model import Model
from test_model import test_model

def visualise(model: Model):
    """
    This function creates a visualisation of a model using Matplotlib
    
    """

    #plot
    fig, ax = plt.subplots()

    # plot all stations on grid with station name
    for station in model.stations.values():
        x, y = station.location
        ax.plot(x, y, 'o')
        ax.annotate(station.name, (x, y), textcoords="offset points", xytext=(5,5), ha='center')
    
    # plot routes

    # create color cycle
    colors = cycle(plt.cm.tab10.colors)

    for route in model.routes.values():
        # Extract x and y coordinates for each station in the route
        route_x = [station.location[0] for station in route.stations]
        route_y = [station.location[1] for station in route.stations]
        
        # Plot line connecting the stations
        color = next(colors)
        ax.plot(route_x, route_y, color = color)
        
    # add titles
    ax.set_title("Stations + Routes")
    
    # display plot
    plt.show()
    

if __name__ == '__main__':
    visualise(test_model())