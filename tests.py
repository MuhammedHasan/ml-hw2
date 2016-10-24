import unittest
import cPickle as pickle

import feature_extraction
import learning_phase
import custom_model
from grid import Grid
from mdp import MarkowModel


class TestFeatureExtraction(unittest.TestCase):

    def setUp(self):
        self.point = (5, 3)
        self.point1 = (6, 3)
        self.matrix = [
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 1, 0, 0, 2],
            [2, 1, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 1, 0, 1, 2],
            [2, 0, 0, 1, 0, 0, 3, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
        ]

    def tests_feature_set_1(self):
        fs = feature_extraction.feature_set_1(self.point, self.matrix)
        self.assertEqual(fs, [2, 4, 5, 3])

        fs = feature_extraction.feature_set_1(self.point1, self.matrix)
        self.assertEqual(fs, [1, 4, 6, 3])

    def tests_feature_set_2(self):
        fs = feature_extraction.feature_set_2(self.point, self.matrix)
        self.assertEqual(fs, [0, 1, 2, 2])

        fs = feature_extraction.feature_set_2(self.point1, self.matrix)
        self.assertEqual(fs, [0, 0, 1, 1])

    def tests_feature_set_3(self):
        f9 = feature_extraction.feature_set_3(self.point, self.matrix)
        self.assertEqual(f9, 5)

        f9 = feature_extraction.feature_set_3(self.point1, self.matrix)
        self.assertAlmostEqual(f9, 5.83095189)

    def tests_get_exits_from_grid(self):
        exists = feature_extraction.get_exits_from_grid(self.matrix)
        self.assertEqual(exists[0, 0], -10)
        self.assertEqual(exists[2, 2], -5)
        self.assertEqual(exists[3, 2], -5)
        self.assertEqual(exists[4, 1], -5)
        self.assertEqual(exists[6, 6], 30)


class TestLearningPhase(unittest.TestCase):

    def setUp(self):
        self.matrix = [
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 1, 0, 0, 2],
            [2, 1, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 1, 0, 1, 2],
            [2, 0, 0, 1, 0, 0, 3, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
        ]

    def tests_model_(self):
        predictions = learning_phase.eveluate_model(self.matrix)
        self.assertTrue(predictions)

        cro_val_acc = learning_phase.check_accurcy(dataset='training_data')
        print '\ndefault model'
        print 'cross validation accuracy:', cro_val_acc
        print 'test accuracy:', learning_phase.check_accurcy()


class TestCustomModel(unittest.TestCase):

    def setUp(self):
        self.matrix = [
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 1, 0, 0, 2],
            [2, 1, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 1, 0, 1, 2],
            [2, 0, 0, 1, 0, 0, 3, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
        ]

    def tests_model_(self):
        predictions = learning_phase.eveluate_model(self.matrix)
        self.assertTrue(predictions)

        cro_val_acc = learning_phase.check_accurcy(
            dataset='training_data', model=custom_model.eveluate_model)

        print '\ncustom model'
        print 'cross validation accuracy:', cro_val_acc
        print 'test accuracy:', learning_phase.check_accurcy(
            model=custom_model.eveluate_model)


if __name__ == '__main__':
    unittest.main()
