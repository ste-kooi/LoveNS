import copy
from classes.model import Model
from classes.station import Station
from classes.route import Route
from classes.connection import Connection
from algorithms.depth_first import Depth_first_route

class Breadth_first_route(Depth_first_route):
    def get_next_option(self):
        return self.options.pop(0)