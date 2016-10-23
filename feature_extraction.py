# -*- coding: utf-8 -*-
import numpy as np
import math


def feature_set_1(point, grid):
    """Computes the distance from the agent to the dark blue squares aligned
       with it
       Parameters
       ----------
       point: (x,y) the position of the agent in the grid
       grid: 2d array representing a grid
       Returns
       -------
       [f1,f2,f3,f4]: a list of features in the given format
       """
    return [7 - point[0], 7 - point[1], point[0], point[1]]


def feature_set_2(point, grid):
    """Computes the distance from the agent to the light blue squares
       one unit away from it
       Parameters
       ----------
       point: (x,y) the position of the agent in the grid
       grid: 2d array representing a grid
       Returns
       -------
       [f5,f6,f7,f8]: a list of features in the given format
       """

    x, y = 7 - point[0], point[1]
    f5 = grid[x - 1][y - 1:y + 2]
    f7 = grid[x + 1][y - 1:y + 2]
    f6 = zip(*grid)[y + 1][x - 1:x + 2]
    f8 = zip(*grid)[y - 1][x - 1:x + 2]

    return [sum(filter(lambda x: x == 1, i)) for i in [f5, f6, f7, f8]]


def feature_set_3(point, grid):
    """Computes the distance from the agent to the green square
       Parameters
       ----------
       point: (x,y) the position of the agent in the grid
       grid: 2d array representing a grid
       Returns
       -------
       f9: type- float
       """
    return math.sqrt(pow(point[0] - 1, 2) + pow(6 - point[1], 2))


def feature_set_4(point, grid):
    """Computes the distance from the agent to the green square
       Parameters
       ----------
       point: (x,y) the position of the agent in the grid
       grid: 2d array representing a grid
       Returns
       -------
       f9: type- float
       """
    return grid[7 - point[0]][point[1]]


def feature_set(point, grid):
    """Computes the all features
       Parameters
       ----------
       point: (x,y) the position of the agent in the grid
       grid: 2d array representing a grid
       Returns
       -------
       [f1,f2,f3,f4,f5,f6,f7,f8,f9]: a list of features in the given format
       """
    return feature_set_1(point, grid) + feature_set_2(point, grid) \
        + [feature_set_3(point, grid)]


def custom_feature_set(point, grid):
    return feature_set(point, grid) + [feature_set_4(point, grid)]
