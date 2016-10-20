# -*- coding: utf-8 -*-
import pickle


dataset = pickle.load(open('training_data.p', 'rb'))

for j in dataset.values():
    for i in j[0]:
        print i
    print


def eveluate_model(grid):
    """For a given grid, return the policy for that grid
       Parameters
       ----------
       grid: 2 dimensional array representing a grid
       Return:
       policy: type-dictionary, for states (1,1) up to (6,6)
       """
    policy = {}
    return policy
