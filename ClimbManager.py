"""
Author:     Alistair Lee
Goal:       An object to manage the different Climb and Log objects
Created:    06/03/2020
"""
from Climb import Climb
from Log import Log
import os
import csv
from datetime import date as dt_date, timedelta
from operator import itemgetter
from matplotlib import pyplot as plt


class ClimbManager:
    """
    An object to manage the different Climb and Log objects
    """

    DIRECTORY = 'Logbooks'  # Static location of the directory of the Logbooks

    def __init__(self):
        """
        When defining the object don't pass any arguments but create an empty set of climbs and empty list of logbook
        """
        self._climbs = set()
        self._logbook = []

    def add_climb(self, climb: Climb):
        self._climbs.add(climb)

    def add_log(self, climb: Log):
        self._logbook.append(climb)

    def get_climbs(self):
        return self._climbs

    def get_logbook(self):
        return self._logbook

    def get_climbs_in_climb(self):
        """
        Get a list of the unique climbs in the set of climbs

        :return: Name + '_' + crag of each climb
        """
        return [climb.name_crag() for climb in self.get_climbs()]

    def load_climbs(self, ukc_name: str):
        """
        Load all the climbs for a climber, saving all the individual climbs to the climbs set and all instances of
        these cimbs to the logbook.

        :param ukc_name: The UKC name of a climber
        :return: All climb information loaded
        """
        # Get the logbook file name for the climber
        log_book = [file for file in os.listdir(ClimbManager.DIRECTORY) if file.split('_')[0] == ukc_name][0]
        with open(ClimbManager.DIRECTORY + '\\' + log_book) as file:  # Load the file
            read_csv = csv.reader(file)
            first = True  # First line contains the header so skip
            for row in read_csv:
                if first:
                    first = False
                    continue
                name = row[0]
                # When downloading info from UKC the grades and stars are located together
                # Seperate this information, store the grade and count the stars
                grade_info = row[1].split(' ')
                grade = ' '.join(grade_info[:-1])
                grade = grade.rstrip()
                stars = len(grade_info[-1])
                climb_style = row[2]
                # The grade of the route hides information about what kind of route it is, trad/sport/boulder etc.
                style = self.find_style(grade)
                partners = row[3].split(', ')
                notes = row[4]
                # Get the date the route was done
                date = self.determine_date(row[5])
                crag = row[6]
                climb = Climb(name, style, grade, stars, crag)  # Create a Climb object and add
                if name + '_' + crag not in self.get_climbs_in_climb():  # If the climb not loaded then load
                    self.add_climb(climb)
                    log = Log(date, climb_style, partners, notes, climb)  # Create a Log object and append
                    self.add_log(log)
                else:
                    # Find the correct climb and add a log of that climb
                    load_climb = [climb for climb in self.get_climbs() if climb.name_crag() == name + '_' + crag][0]
                    log = Log(date, climb_style, partners, notes, load_climb)  # Create a Log object and append
                    self.add_log(log)

    @staticmethod
    def find_style(grade: str) -> str:
        """
        The grade hides information about what kind of route the climb is, e.g. trad/sport/winter etc.
        Pull this information about the climb

        NB: this will only determine UK grades, any other (e.g. american, SA et.) will end up being saved as sport

        :param grade: The grade of the route from UKC
        :return: A type of route
        """
        if len(grade) == 0:  # Some routes don't contain this information
            return 'none'
        elif 'summit' in grade:  # Summit tops can also be recorded
            return 'walk'
        # Trad routes contain the following information
        elif grade[0] in ['E', 'S', 'D'] or grade[:2] in ['VS', 'VD', 'HS', 'HD'] or grade[:3] in ['HVS', 'HVD', 'MVS']:
            return 'trad'
        elif len(grade) == 1 and grade == 'M':
            return 'trad'
        # Boulder routes start with an f or v followed by a grade (if just a v then it's a winter route)
        elif grade[0].lower() == 'f' or (grade[0].lower() == 'v' and grade[1].isnumeric()):
            return 'boulder'
        # If the route starts with an roman numeral then it must be a winter climb
        elif grade[0] in ['I', 'V', 'X']:
            return 'winter'
        elif 'S' in grade:  # Since a trad route is captured any remaining routes with an S will be a DWS
            return 'dws'
        elif grade[0] == 'M':  # Tooling routes will being with an M
            return 'dry tool'
        else:
            return 'sport'  # Everything else must be a sport route

    @staticmethod
    def determine_date(date: str):
        """
        When downloading from UKC dates come through in a rather messy way, this function makes assumptions and fixes
        this.

        :param date: The date as it comes from UKC
        :return: A date object
        """
        calander = {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr': 4,
            'may': 5,
            'jun': 6,
            'jul': 7,
            'aug': 8,
            'sep': 9,
            'oct': 10,
            'nov': 11,
            'dec': 12
        }  # A calander that can be used to map the str months to numerical months
        if date[:3] == '???':  # When no day or month is recorded then ??? preceeds the year
            return dt_date(int(date[-4:]), 1, 1)
        elif date[:2] == '??':  # When no month is recorded then ?? preceeds the month and year
            month = calander[date[3:6].lower()]  # Find the numerical month
            return dt_date(int('20' + date[-2:]), month, 1)
        else:  # Otherwise all date information is given and determine the date
            month = calander[date[3:6].lower()]  # Find the numerical month
            return dt_date(int('20' + date[-2:]), month, int(date[:2]))

    def climbs_of_type(self, climb_type: str):
        for climb in self.get_logbook():
            if climb.get_climb().get_style() == climb_type:
                yield climb

    def routes_by_month(self):
        months = {}
        for climb in self.get_logbook():
            if climb.get_climb().get_style() == 'walk':
                continue
            elif self.round_date_down(climb.get_date()) in months.keys():
                month = months[self.round_date_down(climb.get_date())]
                month.append(climb.get_climb())
            else:
                months[self.round_date_down(climb.get_date())] = [climb.get_climb()]
        return months

    def plot_sport(self):
        fig, ax = plt.subplots()
        for climb in self.get_logbook():
            if climb.get_climb().get_style() != 'sport':
                continue
            ax.scatter(climb.get_date(), climb.get_climb().get_points(),
                       s=climb.get_climb().get_stars(), label=climb.get_climb().get_name())
        labels = [item for item in ax.get_yticks()]
        for label in labels:
            ind = labels.index(label)
            
        ax.set_yticklabels(['7C', '9a'])
        plt.ylim(0,1)
        plt.show()

    @staticmethod
    def get_most_type_climbs(list_climbs: list) -> str:
        types = {}
        for climb in list_climbs:
            if climb.get_style() in types.keys():
                types[climb.get_style()] += 1
            else:
                types[climb.get_style()] = 1
        return max(types.items(), key=itemgetter(1))[0]

    @staticmethod
    def round_date_down(date: dt_date):
        return date - timedelta(date.day - 1)

