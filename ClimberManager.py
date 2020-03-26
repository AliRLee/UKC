"""
Author:     Alistair Lee
Goal:       An object to manage the different Climber objects
Created:    06/03/2020
"""
import csv
from Climber import Climber
import matplotlib.cm as cm
import numpy as np


class ClimberManager:
    """
    An object to manage the different Climber objects
    """

    CLIMBERS_CSV = 'Climbers\\Climbers.csv'  # Static location of the climbers

    def __init__(self):
        """
        When defining the object don't pass any attributes but create a blank list of climbers
        and load all the climbers
        """
        self._climbers = []
        self.load_all()

    def add_climber(self, climber):
        self._climbers.append(climber)

    def get_climbers(self):
        return self._climbers

    def load_climbers(self):
        """
        Load the climbers to the list of climbers.

        :return: All climbers added to the list of climbers
        """
        with open(ClimberManager.CLIMBERS_CSV) as file:  # Open the file with climbers
            read_csv = csv.reader(file)
            first = True  # Ignore the first row as it is the header row
            for row in read_csv:
                if first:
                    first = False
                    continue
                first_name = row[0]
                last_name = row[1]
                ukc_name = row[2]
                age = int(row[3])
                height = float(row[4])
                weight = float(row[5])
                sex = row[6]
                nationality = row[7]
                # Create the climber object now all info is loaded
                climber = Climber(first_name, last_name, ukc_name, age, height, weight, sex, nationality)
                self.add_climber(climber)  # Add the newly created climber

    def load_climbers_climbs(self):
        """
        For every climber load their climbs, if there is not a logbook for that climber then don't do anything

        :return: Climbs loaded to climbers if their logbook exists
        """
        for climber in self.get_climbers():  # Loop over climbers
            try:  # Try to load their climbs, if you get an error due to their being no file, do nothing
                climber.load_climbs()
            except IndexError:
                pass

    def load_all(self):
        """
        Load all the climbers then load all the climbs for every climber

        :return: All data loaded
        """
        self.load_climbers()
        self.load_climbers_climbs()

    def get_climber(self, climber_name: str) -> Climber:
        try:
            return [climber for climber in self.get_climbers() if climber.get_name() == climber_name][0]
        except IndexError:
            print('Use the climbers full name both names capitalized with a space')

    # def plot_climbers_month(self):
    #     cmap = cm.get_cmap('viridis')
    #     map = [cmap(i) for i in np.arange(len(self.get_climbers()))]
    #
    #     for climber, colour in zip(self.get_climbers(), map):
    #         if len(climber.get_logbook()) == 0:
    #             continue
    #         climber.plot_routes_month(colour)
