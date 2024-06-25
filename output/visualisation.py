from classes.model import Model
import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np


def visualise(model: Model, file_path: str):
    """
    This function creates a visualisation of a model using Matplotlib
    Writes figure to file_path.png

    """

    #plot
    fig, ax = plt.subplots(figsize=(15,9))

    # plot all stations on grid with station name
    for station in model.stations.values():
        x, y = station.location
        ax.plot(x, y, 'o')
        ax.annotate(station.name, (x, y), textcoords="offset points", xytext=(5,5), ha='center', size=7)

    # plot routes

    # create color cycle
    colors = cycle(plt.cm.tab20.colors)

    for route in model.routes.values():
        # Extract x and y coordinates for each station in the route
        route_x = np.array([station.location[0] for station in route.stations])
        route_y = np.array([station.location[1] for station in route.stations])

        # Apply a small random offset to separate overlapping lines
        offset_x = np.random.uniform(-0.01, 0.01, size=route_x.shape)
        offset_y = np.random.uniform(-0.01, 0.01, size=route_y.shape)
        route_x += offset_x
        route_y += offset_y

        # Plot line connecting the stations
        color = next(colors)
        ax.plot(route_x, route_y, color = color)

    # add titles and change layout
    ax.set_title(f"Lijnvoering {model.mapname}")
    plt.axis('off')


    # display plot
    plt.savefig(f'{file_path}.png', bbox_inches= 'tight', pad_inches=0)
    print(f"Figure has been saved to {file_path}.png")
