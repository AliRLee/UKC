"""
Author:     Alistair Lee
Goal:       An object of an instance of doing a climb
Created:    06/03/2020
"""
from datetime import date as dt_date
from Climb import Climb


class Log:
    """
    An object of an instance of a climb, allows a climb to be done multiple times.
    """

    def __init__(self, date: dt_date, style: str, partners: list, notes: str, climb: Climb):
        """
        When creating a log pass all essential information about the instance of the climb, where the style will need
        to be corrected.

        :param date: The date the climb was completed
        :param style: The style the climb was completed in, e.g. flash, onsight etc.
        :param partners: A list of people the climber did the climb with
        :param notes: Notes made about the climb, generally a long string
        :param climb: The climb that was completed
        """
        self._date = date
        self._styles = {
            'Lead RP': 'read point',
              'AltLd O/S': 'onsight',
              'Solo O/S': 'onsight',
              'Lead rpt': 'no log',
              'Lead O/S': 'onsight',
              '2nd &beta;': 'flash',
              'Solo rpt': 'no log',
              'Lead Flash': 'flash',
              'Lead dog': 'no send',
              '2nd O/S': 'onsight',
              'AltLd rpt': 'no log',
              'AltLd': 'no log',
              '2nd': 'no log',
              'Sent x': 'read point',
              'Sent Flash': 'flash',
              '-': 'summit',
              'Solo': 'no log',
              'Sent O/S': 'onsight',
              'AltLd dnf': 'no send',
              'Lead dnf': 'no send',
              'DWS': 'no log',
              '2nd rpt': 'no log',
              '2nd dog': 'no send',
              'AltLd dog': 'no send',
              'Sent rpt': 'no log',
              'Lead G/U': 'ground up',
              'Sent': 'no log',
              'Solo dnf': 'no send',
              'Lead': 'no log'}  # A matcher of different style types
        self._style = self.match_style(style)  # Correct the style for a more readable format
        self._partners = partners
        self._notes = notes
        self._climb = climb

    def set_date(self, date):
        self._date = date

    def set_style(self, style):
        self._style = style

    def set_partners(self, partners: list):
        self._partners = partners

    def set_notes(self, notes):
        self._notes = notes

    def set_climb(self, climb):
        self._climb = climb

    def add_style_to_styles(self, style_key: str, style_value: str):
        """
        If the found style is not in the dictionary of styles then add the style to the dictionary.

        :param style_key: The key of UKC style
        :param style_value: The value of the more readable type of style
        :return: New style added
        """
        self._styles[style_key] = style_value

    def get_date(self) -> dt_date:
        return self._date

    def get_style(self) -> str:
        return self._style

    def get_styles(self):
        return self._styles

    def get_partners(self) -> list:
        return self._partners

    def get_notes(self) -> str:
        return self._notes

    def get_climb(self) -> Climb:
        return self._climb

    def get_style_from_styles(self, style_key: str):
        return self._styles[style_key]

    def get_log(self) -> tuple:
        return self.get_date(), self.get_climb()

    def match_style(self, input_style: str) -> str:
        """
        Correct the UKC style to a more readable type of style, using the already created list of styles.
        If the style isn't in the already created dictionary then ask the user what style it is, then add.

        :param input_style: The UKC type of style
        :return: The more readable type of style
        """
        try:  # Try to get from the dictionary
            return self.get_style_from_styles(input_style)
        except KeyError:  # If you get a key error, it is not in the dictionary
            new_style = input(input_style + '\nWhat style is this?')  # Ask the user what style it is
            self.add_style_to_styles(input_style, new_style)  # Add this style to the dictionary
            return new_style  # Return the more readable style
