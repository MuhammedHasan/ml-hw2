# -*- coding: utf-8 -*-
import pickle
import learning_phase


svm = learning_phase.train_model(
    feature_selection=learning_phase.custom_feature_set,
    C=1000.0, filename="custom_model.p")


def eveluate_model(grid):
    """For a given grid, return the policy for that grid
       Parameters
       ----------
       grid: 2 dimensional array representing a grid
       Return:
       policy: type-dictionary, for states (1,1) up to (6,6)
       """
    return learning_phase.eveluate_model(
        grid, feature_selection=learning_phase.custom_feature_set, model=svm)
