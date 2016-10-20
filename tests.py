import unittest
import feature_extraction
import learning_phase
import cPickle as pickle


class TestFeatureExtraction(unittest.TestCase):

    def setUp(self):
        self.point = (2, 3)
        self.point1 = (1, 3)
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


class LearningPhaseExtraction(unittest.TestCase):

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

    def tests_(self):

        print learning_phase.check_accurcy()

        # predictions = learning_phase.eveluate_model(self.matrix)
        #
        # print predictions

        # self.assertTrue(model)

if __name__ == '__main__':
    unittest.main()
