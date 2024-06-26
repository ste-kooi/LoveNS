from classes.model import Model
import random


def test_model():
    """
    This function returns a model with the stations from the test output file
    
    """
    model = Model('Holland')

    # Route 1
    model.add_route(model.stations['Beverwijk'], 1)
    model.routes[1].add_station(model.stations['Castricum'])
    model.routes[1].add_station(model.stations['Alkmaar'])
    model.routes[1].add_station(model.stations['Hoorn'])
    model.routes[1].add_station(model.stations['Zaandam'])

    # Route 2
    model.add_route(model.stations['Amsterdam Sloterdijk'], 2)
    model.routes[2].add_station(model.stations['Amsterdam Centraal'])
    model.routes[2].add_station(model.stations['Amsterdam Amstel'])
    model.routes[2].add_station(model.stations['Amsterdam Zuid'])
    model.routes[2].add_station(model.stations['Schiphol Airport'])

    # Route 3
    model.add_route(model.stations['Rotterdam Alexander'], 3)
    model.routes[3].add_station(model.stations['Gouda'])
    model.routes[3].add_station(model.stations['Alphen a/d Rijn'])
    model.routes[3].add_station(model.stations['Leiden Centraal'])
    model.routes[3].add_station(model.stations['Schiphol Airport'])
    model.routes[3].add_station(model.stations['Amsterdam Zuid'])

    return model

def test_model_nl():
    """
    This function returns a model with the stations from the test output file
    
    """
    model = Model('Nederland')

    # Route 1
    model.add_route(model.stations['Alkmaar'], 1)
    model.routes[1].add_station(model.stations['Hoorn'])
    model.routes[1].add_station(model.stations['Zaandam'])
    model.routes[1].add_station(model.stations['Amsterdam Sloterdijk'])
    model.routes[1].add_station(model.stations['Haarlem'])

    # Route 2
    model.add_route(model.stations['Den Haag Centraal'], 2)
    model.routes[2].add_station(model.stations['Gouda'])
    model.routes[2].add_station(model.stations['Alphen a/d Rijn'])
    model.routes[2].add_station(model.stations['Leiden Centraal'])
    model.routes[2].add_station(model.stations['Schiphol Airport'])

    # Route 3
    model.add_route(model.stations['Maastricht'], 3)
    model.routes[3].add_station(model.stations['Sittard'])

    return model

