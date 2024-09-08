# tests/test_sand_simulation.py

import unittest

import numpy as np

from pixel_pour.simulation.sand_simulation import SandSimulation
from pixel_pour.utils.config import MAX_FALL_SPEED


class TestSandSimulation(unittest.TestCase):
    """
    Class for testing SandSimulation.
    """

    def setUp(self):
        """
        Set up the simulation with a 200x200 grid.
        :return: None
        """
        self.width = 200
        self.height = 200
        self.simulation = SandSimulation(self.width, self.height)

    def test_initialization(self):
        """
        Test that the simulation is initialized properly with a correctly sized grid.
        :return: None
        """
        self.assertEqual(self.simulation.width, self.width)
        self.assertEqual(self.simulation.height, self.height)
        self.assertEqual(len(self.simulation.sand_grains), 0)
        self.assertEqual(self.simulation.grid.shape, (self.height, self.width))

    def test_add_sand(self):
        """
        Test that the sand is added to the simulation.
        :return: None
        """
        self.simulation.add_sand(5, 5)
        self.assertEqual(len(self.simulation.sand_grains), 1)
        self.assertTrue(self.simulation.grid[5, 5])
        np.testing.assert_array_almost_equal(self.simulation.sand_grains[0], [5, 5, 0])

    def test_add_sand_out_of_bounds(self):
        """
        Test that the sand is not added to the simulation when added out-of-bounds.
        :return: None
        """
        self.simulation.add_sand(-1, -1)
        self.simulation.add_sand(self.width, self.height)
        self.assertEqual(len(self.simulation.sand_grains), 0)

    def test_sand_falls(self):
        """
        Test that the sand added falls with gravity.
        :return: None
        """
        self.simulation.add_sand(10, 5)
        for _ in range(10):  # Update many times
            self.simulation.update()
        self.assertGreater(int(self.simulation.sand_grains[0, 1]), 5)
        self.assertTrue(
            self.simulation.grid[int(self.simulation.sand_grains[0, 1]), 10]
        )

    def test_sand_stops_at_bottom(self):
        """
        Test that the sand stops at the bottom of the grid.
        :return: None
        """
        self.simulation.add_sand(15, self.height - 1)
        initial_y = self.simulation.sand_grains[0, 1]
        for _ in range(10):  # Update multiple times
            self.simulation.update()
        self.assertEqual(self.simulation.sand_grains[0, 1], initial_y)

    def test_sand_piles_up(self):
        """
        Test that the sand piles up in the grid.
        :return:
        """
        self.simulation.add_sand(20, self.height - 1)
        self.simulation.add_sand(20, self.height - 3)
        for _ in range(100):  # Update many times
            self.simulation.update()
        self.assertEqual(int(self.simulation.sand_grains[0, 1]), self.height - 1)
        self.assertEqual(int(self.simulation.sand_grains[1, 1]), self.height - 2)

    def test_sand_cascades(self):
        """
        Test that the sand cascades when stacked too tall.
        :return:
        """
        # Create a stack of 3 grains
        self.simulation.add_sand(25, self.height - 1)
        self.simulation.add_sand(25, self.height - 2)
        self.simulation.add_sand(25, self.height - 3)
        for _ in range(100):  # Update many times
            self.simulation.update()
        # The top grain should have moved left or right
        top_grain = self.simulation.sand_grains[2]
        self.assertNotEqual(int(top_grain[0]), 5)
        self.assertIn(int(top_grain[0]), [24, 26])

    def test_sand_accelerates(self):
        """
        Test that gravity is causing the sand to accelerate.
        :return: None
        """
        self.simulation.add_sand(30, 0)
        initial_velocity = float(self.simulation.sand_grains[0, 2])
        self.simulation.update()
        final_velocity = float(self.simulation.sand_grains[0, 2])
        self.assertGreater(final_velocity, initial_velocity)

    def test_terminal_velocity(self):
        """
        Test that the sand does not exceed the terminal velocity.
        :return: None
        """
        self.simulation = SandSimulation(self.width, 1000)  # Taller simulation
        self.simulation.add_sand(35, 0)
        for _ in range(100):  # Update many times
            self.simulation.update()
        self.assertAlmostEqual(
            float(self.simulation.sand_grains[0, 2]), MAX_FALL_SPEED, places=1
        )


if __name__ == "__main__":
    unittest.main()
