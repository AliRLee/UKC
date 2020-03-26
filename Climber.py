"""
Author:     Alistair Lee
Goal:       A climber object, holding all information about a climber
Created:    06/03/2020
"""
from ClimbManager import ClimbManager as cm
from matplotlib import pyplot as plt
from collections import OrderedDict
from datetime import date as dt_date, timedelta
import numpy as np


class Climber:
    """
    A climber object, holding all information about a climber
    """

    def __init__(self, first_name: str, last_name: str, ukc_name: str, age: int,
                 height: float, weight: float, sex: str, nationality: str):
        """
        When defining a climber pass all essential information about a climber

        :param first_name: First (given) name of a climber
        :param last_name: Last (family) name of a climber
        :param ukc_name: The username on UKC
        :param age: The age of a climber, int  # years
        :param height: The height of a climber, float  # cm
        :param weight: The weight of a climber, float  # kg
        :param sex: The sex of a climber, M/F
        :param nationality: The nationality of a climber
        """
        self._first_name = first_name
        self._last_name = last_name
        self._ukc_name = ukc_name
        self._age = age  # years
        self._height = height  # cm
        self._weight = weight  # kg
        self._sex = sex  # M/F
        self._nationality = nationality
        self._climbs = cm()

    def get_first_name(self) -> str:
        return self._first_name

    def get_last_name(self) -> str:
        return self._last_name

    def get_ukc_name(self) -> str:
        return self._ukc_name

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def get_weight(self) -> float:
        return self._height

    def get_sex(self) -> str:
        return self._sex

    def get_nationality(self) -> str:
        return self._nationality

    def get_name(self) -> str:
        """
        Return the full name of a climber, an addition of their first name and last name

        :return: Full name, str
        """
        return self.get_first_name().capitalize() + ' ' + self.get_last_name()

    def get_climb_manager(self) -> cm:
        return self._climbs

    def load_climbs(self):
        """
        Load all climbs for this climber, using their UKC logbook.

        :return: Climbs loaded
        """
        self.get_climb_manager().load_climbs(self.get_ukc_name())

    def get_climbs(self):
        """
        Get the climbs the climber has done

        :return: Set of Climb objects
        """
        return self.get_climb_manager().get_climbs()

    def get_logbook(self) -> list:
        """
        Get the logbook of climbs the climber has done

        :return: List of Log objects
        """
        return self.get_climb_manager().get_logbook()

    def get_routes_climbed(self):
        """
        Return the number of routes the user has done.

        :return: Number of routes the climber has completed
        """
        return len(self.get_climbs())

    def get_climbs_done(self):
        """
        Return the number of instances of climbs the climber has done

        :return: Total length of the logbook
        """
        return len(self.get_logbook())

    def plots_routes_time(self, route_type='all'):
        plt.close()
        if route_type == 'all':
            colours = {
                'sport': 'm',
                'trad': 'g',
                'winter': 'c',
                'boulder': 'r',
                'none': 'k',
                'dws': 'b',
                'dry tool': 'y'
                      }

            for climb in self.get_logbook():
                date = climb.get_date()
                points = climb.get_climb().get_points()
                style = climb.get_climb().get_style()
                if style in colours.keys():
                    colour = colours[style]
                else:
                    colour = 'k'
                plt.scatter(date, points, color=colour, label=style)
            handles, labels = plt.gca().get_legend_handles_labels()
            by_label = OrderedDict(zip(labels, handles))
            plt.legend(by_label.values(), by_label.keys())
            plt.show()
        else:
            for climb in self.get_climb_manager().climbs_of_type(route_type):
                date = climb.get_date()
                points = climb.get_climb().get_points()
                plt.scatter(date, points, color='blue')
            plt.show()

    def plot_routes_month(self, climber_colour=''):
        months = self.get_climb_manager().routes_by_month()
        colours = {
            'sport': 'm',
            'trad': 'g',
            'winter': 'c',
            'boulder': 'r',
            'none': 'k',
            'dws': 'b',
            'dry tool': 'y'
        }
        for month, climbs in months.items():
            avg_points = np.mean([climb.get_points() for climb in climbs])
            style = self.get_climb_manager().get_most_type_climbs(climbs)
            if style in colours:
                colour = colours[style]
            else:
                colour = 'k'
            if climber_colour == '':
                climber_colour = 'white'
            plt.scatter(month, avg_points, s=len(climbs)*20, edgecolors=colour, alpha=0.5,
                        label=style, color=climber_colour, linewidth=2)
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys(), title='Most Popular\nStyle')
        plt.ylabel('Normalised Difficulty')
        plt.show()


