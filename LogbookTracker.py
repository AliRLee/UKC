"""
Author:     Alistair Lee
Goal:       A place to start investigating the climbs undertaken by the climbers
Created:    06/03/2020

NB: To add more climbers to this:
    - Download your logbook from ukclimbing.com -> my logbook
    - Find and replace all instances of β for Flash
    - Save the file as a .csv in Logbooks
    - Add static information about the new climber to the csv in Climbers\\Climbers.csv

"""
from ClimberManager import ClimberManager

from matplotlib import pyplot as plt
from collections import OrderedDict
from datetime import date as dt_date, timedelta
import numpy as np

climber_tracker = ClimberManager()

climber = climber_tracker.get_climber('Alistair Lee')

# print(climber.get_routes_climbed())
# print(climber.get_climbs_done())
#
# print(climber.get_logbook()[0].get_date(), '\n',
#       climber.get_logbook()[0].get_climb().get_name(), '\n',
#       climber.get_logbook()[0].get_notes(), '\n',
#       climber.get_logbook()[0].get_climb().get_points())

# climber.routes_by_month()
# climber_tracker.get_climber('Alistair Gilmour').plot_routes_month('orange')
# climber_tracker.get_climber('Alistair Lee').plot_routes_month('')

climber.get_climb_manager().plot_sport()

# climber_colour = ''
#
# months = climber.get_climb_manager().routes_by_month()
# colours = {
#     'sport': 'm',
#     'trad': 'g',
#     'winter': 'c',
#     'boulder': 'r',
#     'none': 'k',
#     'dws': 'b',
#     'dry tool': 'y'
# }

# fig, ax = plt.subplots()
# for month, climbs in months.items():
#     avg_points = np.mean([climb.get_points() for climb in climbs])
#     style = climber.get_climb_manager().get_most_type_climbs(climbs)
#     if style in colours:
#         colour = colours[style]
#     else:
#         colour = 'k'
#     if climber_colour == '':
#         climber_colour = 'white'
#     ax.scatter(month, avg_points, s=len(climbs) * 20, edgecolors=colour, alpha=0.5,
#                 label=style, color=climber_colour, linewidth=2)
# handles, labels = plt.gca().get_legend_handles_labels()
# by_label = OrderedDict(zip(labels, handles))
# ax.legend(by_label.values(), by_label.keys(), title='Most Popular\nStyle')
# plt.ylabel('Normalised Difficulty')
# # plt.show()
# plt.ylim(0)
#
# labels = [item for item in ax.get_yticks()]
#
# labels[1] = 'test'
#
# ax.set_yticklabels(labels)
#
# plt.show()