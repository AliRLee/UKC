"""
Author:     Alistair Lee
Goal:       Create a list of all climbing grades for the different styles and give these grades a score dependant on
            their difficulty.
Created:    09/03/2020
"""


def get_score(my_list) -> dict:
    """
    Given a list of grades, score these depending on the difficulty.
    Assumes the list is in order of difficulty

    :param my_list: List of climbing grades
    :return: A dictionary of the grades and their score
    """
    points = {}
    for grade, index in zip(my_list, range(1, len(my_list) + 1)):
        points[grade] = index/len(my_list)
    return points


# Create functions that add the letter part of the grade
fa = lambda x: str(x) + 'a'
fap = lambda x: str(x) + 'a+'
fb = lambda x: str(x) + 'b'
fbp = lambda x: str(x) + 'b+'
fc = lambda x: str(x) + 'c'
fcp = lambda x: str(x) + 'c+'

"""
Create lists of climbing grades
"""

sport = [f(x) for x in range(4, 10) for f in (fa, fap, fb, fbp, fc, fcp)]
sport.remove('9c+')
sport.insert(0, '4+')
sport.insert(0, '4')
sport.insert(8, '5+')
sport.insert(8, '5')
sport.insert(0, '2a')
sport.insert(0, '2')
sport.insert(0, '1')

boulder_fb = ['f' + f(x).upper() for x in range(4, 9) for f in (fa, fap, fb, fbp, fc, fcp)]
boulder_fb.append('f9a')
boulder_fb.insert(0, 'f4+')
boulder_fb.insert(0, 'f4')
boulder_fb.insert(8, 'f5+')
boulder_fb.insert(8, 'f5')
boulder_fb.insert(0, 'f3+')

boulder_v = ['V' + str(x) for x in range(18)]

trad = ['M', 'D', 'VD', 'HD', 'HVD', 'S', 'MS', 'VS', 'HS', 'MVS', 'HVS']
trad_add = ['E' + str(x) for x in range(1,12)]
trad.extend(trad_add)

winter = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI']

dry_tool = ['M' + str(x) for x in range(0, 14)]

"""
Create the dictionary of points using the get_score function
"""

sport_points = get_score(sport)
boulder_fb_points = get_score(boulder_fb)
boulder_v_points = get_score(boulder_v)
trad_points = get_score(trad)
summit_points = {'summit': 1}
winter_points = get_score(winter)
dry_tool_points = get_score(dry_tool)

# Create a dictionary of all the different score dictionaries and their key
points = {
    'sport': sport_points,
    'boulder_fb': boulder_fb_points,
    'boulder_v': boulder_v_points,
    'trad': trad_points,
    'walk': summit_points,
    'winter': winter_points,
    'dws': sport_points,
    'none': {'none': 0},
    'dry tool': dry_tool_points
}
