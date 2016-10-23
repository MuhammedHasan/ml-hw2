import unittest
from grid import Grid
from mdp import MarkowModel


class TestGrid(unittest.TestCase):

    def setUp(self):
        self.grid = Grid()
        self.wall = (1, 1)
        self.exit = (0, 3)

    def test_is_wall(self):
        self.assertTrue(self.grid.is_wall(self.wall[0], self.wall[1]))

    def test_is_exit(self):
        self.assertFalse(self.grid.is_exit(self.wall[0], self.wall[1]))
        self.assertTrue(self.grid.is_exit(self.exit[0], self.exit[1]))

    def test_get_V(self):
        self.assertEqual(self.grid.get_V(0, 0), 0)
        self.assertRaises(ValueError, self.grid.get_V,
                          self.wall[0], self.wall[1])
        self.assertRaises(ValueError, self.grid.get_V, 10, 10)

    def test_set_V(self):
        self.grid.set_V(0, 0, 1)
        self.assertEqual(self.grid.get_V(0, 0), 1)
        self.assertRaises(ValueError, self.grid.set_V,
                          self.wall[0], self.wall[1], 1)
        self.assertRaises(ValueError, self.grid.set_V, 10, 10, 10)

    def test_is_out_of_map(self):
        self.assertTrue(self.grid.is_out_of_map(0, -1))
        self.assertFalse(self.grid.is_out_of_map(0, 0))

    def test_outcome_of_action(self):
        self.assertEqual(self.grid.outcome_of_action(0, 0, '^'),
                         {(0, 0): 0.9, (0, 1): 0.1})
        self.assertEqual(self.grid.outcome_of_action(0, 0, 'v'),
                         {(1, 0): 0.8, (0, 1): 0.1, (0, 0): 0.1})
        self.assertEqual(self.grid.outcome_of_action(1, 0, '^'),
                         {(0, 0): 0.8, (1, 0): 0.2})


class TestMarkowModel(unittest.TestCase):

    def setUp(self):
        self.r_value = 0.4
        self.wall = (1, 1)
        self.exit = (0, 3)
        self.markow_model = MarkowModel(Grid(), 0.4)
        self.previous_grid = Grid()
        self.previous_grid.set_V(0, 0, 0.5)
        self.previous_grid.set_V(1, 0, 0.2)
        self.previous_grid.set_V(2, 0, 0.4)

    def test_R(self):
        self.assertEqual(self.markow_model.R(self.exit[0], self.exit[1]), 1)
        self.assertRaises(ValueError, self.markow_model.R,
                          self.wall[0], self.wall[0])

    def test_Q(self):
        self.assertEqual(
            self.markow_model.Q(1, 0, '^', self.previous_grid),
            0.44 + self.r_value)

    def test_Qs(self):
        qs = dict(self.markow_model.Qs(1, 0, self.previous_grid))
        self.assertTrue(0.00000001 >= abs(qs['^'] - (0.44 + self.r_value)))
        self.assertTrue(0.00000001 >= abs(qs['<'] - (0.25 + self.r_value)))
        self.assertTrue(0.00000001 >= abs(qs['>'] - (0.25 + self.r_value)))
        self.assertTrue(0.00000001 >= abs(qs['v'] - (0.36 + self.r_value)))

if __name__ == '__main__':
    unittest.main()
