"""
Author:     Alistair Lee
Goal:       A climb object, holding all information about a climb
Created:    06/03/2020
"""
from Scoring import points


class Climb:
    """
    A climb object containing all information about a climb
    """

    def __init__(self, name: str, style: str, grade: str, stars, crag: str):
        """
        When defining the object pass all the essential information to the object.
        when defining the object will calculate its points depending on the grade of the route.

        :param name: Name of the climb
        :param style: Style of the route, e.g. trad, sport, winter etc.
        :param grade: Grade of the route #TODO further define this so it is numeric
        :param stars: The amount of stars a route gets, maximum is 4
        :param crag: The crag the route is on
        :param points: The points of the route, dependant on the grade of the route
        """
        self._name = name
        self._style = style
        self._grade = grade
        self._stars = stars
        self._crag = crag
        self._points = 0
        self.score()

    def set_name(self, name):
        self._name = name

    def set_style(self, style):
        self._style = style

    def set_grade(self, grade):
        self._grade = grade

    def set_stars(self, stars):
        self._stars = stars

    def set_crag(self, crag):
        self._crag = crag

    def set_points(self, route_points):
        self._points = route_points

    def get_name(self) -> str:
        return self._name

    def get_style(self) -> str:
        return self._style

    def get_grade(self) -> str:
        return self._grade.strip()

    def get_stars(self) -> int:
        return self._stars

    def get_crag(self) -> str:
        return self._crag

    def get_points(self) -> float:
        return self._points

    def name_crag(self) -> str:
        """
        Seeing as there are multiple routes of the same name at different crags it is worth making a unique identifier
        for each route, the route name + crag is sufficient.

        :return: Route name and crag
        """
        return self.get_name() + '_' + self.get_crag()

    def score(self) -> float:
        """
        For a route get the points for that climb, this is dependant on the difficulty of the climb and the type of
        climb.

        :return: The score of a route, an indication of its difficulty
        """
        try:  # Try to find the score
            # Using the points dictionary find the appropriate dictionary of scores
            if self.get_style() == 'boulder' and self.get_grade()[0].lower() == 'f':
                style_points = points['boulder_fb']
            elif self.get_style() == 'boulder' and self.get_grade()[0].lower() == 'v':
                style_points = points['boulder_v']
            elif self.get_style() is None:  # Some routes are not recognised, these get no points
                pass
            # UKC records some routes as not having a grade, these get no points
            elif 'none' in self.get_grade() or 'none' in self.get_style():
                pass
            else:
                style_points = points[self.get_style()]

            # Using the appropriate dictionary find the points for the route grade
            if self.get_style() == 'summit':
                route_points = style_points[self.get_style().split(' ')[0]]
            elif self.get_style() == 'dws':  # DWS has the S grade as well, for now ignore this
                route_points = style_points[self.get_grade().split(' ')[0]]
            elif self.get_style() is None:
                route_points = 0
            elif 'none' in self.get_grade() or 'none' in self.get_style():
                route_points = 0
            else:
                route_points = style_points[self.get_grade().split(' ')[0]]
            self.set_points(route_points)
        except KeyError:  # If the score is not yet recorded then inform the user so it can be added
            print('Please add this score to the appropriate list.\n')
            print(self.get_name() + '\t\'' + self.get_style() + '\'', '\'' + self.get_grade() + '\'')
