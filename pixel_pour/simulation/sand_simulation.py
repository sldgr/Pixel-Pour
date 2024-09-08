# pixel_pour/simulation/sand_simulation.py
from dataclasses import dataclass, field

import numpy as np

from pixel_pour.utils.config import GRAVITY, MAX_FALL_SPEED


@dataclass
class SandSimulation:
    """
    A class to simulate a grid and pixels (sand) falling within it.
    """

    width: int
    height: int
    sand_grains: np.ndarray = field(init=False)
    grid: np.ndarray = field(init=False)

    def __post_init__(self) -> None:
        """
        Setup numpy arrays the grid and sand grains after the SandSimulation class initializes.
        :return: None
        """
        self.sand_grains = np.empty((0, 3), dtype=np.float32)  # x, y, velocity
        self.grid = np.zeros((self.height, self.width), dtype=bool)

    def add_sand(self, x: int, y: int) -> None:
        """
        Add a sand grain to the grid at a given coordinate with zero initial velocity.
        :param x: X coordinate of the sand grain.
        :param y: Y coordinate of the sand grain.
        :return: None
        """
        if 0 <= x < self.width and 0 <= y < self.height and not self.grid[y, x]:
            new_grain = np.array([[x, y, 0]], dtype=np.float32)
            self.sand_grains = np.vstack((self.sand_grains, new_grain))
            self.grid[y, x] = True

    def update(self) -> None:
        """
        Update the simulation, moving any sand grains that can move.
        :return: None
        """
        if len(self.sand_grains) == 0:
            return

        new_grid = self.grid.copy()

        for i in range(len(self.sand_grains)):
            x, y, velocity = self.sand_grains[i]
            int_x, int_y = int(x), int(y)

            # Update velocity
            velocity = min(velocity + GRAVITY, MAX_FALL_SPEED)

            # Calculate new position
            new_y = float(int(y + velocity))
            new_int_y = int(new_y)

            # Remove from old position
            new_grid[int_y, int_x] = False

            # Check if new position is below screen or collides with existing grains
            if new_int_y >= self.height or (
                new_int_y > int_y and new_grid[new_int_y, int_x]
            ):
                # Start from the bottom of the screen or the new position
                check_y = min(new_int_y, self.height - 1)

                # Find the top of the pile
                while check_y > int_y and new_grid[check_y, int_x]:
                    check_y -= 1

                # Place the grain on top of the pile
                new_int_y = check_y
                new_y = float(new_int_y)
                velocity = 0

                # Check if the stack is more than two high
                if (
                    new_int_y < self.height - 2
                    and new_grid[new_int_y + 1, int_x]
                    and new_grid[new_int_y + 2, int_x]
                ):
                    # Check if there are no surrounding grains
                    left_clear = (
                        int_x > 0
                        and not new_grid[new_int_y, int_x - 1]
                        and not new_grid[new_int_y + 1, int_x - 1]
                    )
                    right_clear = (
                        int_x < self.width - 1
                        and not new_grid[new_int_y, int_x + 1]
                        and not new_grid[new_int_y + 1, int_x + 1]
                    )

                    if left_clear or right_clear:
                        # Randomly choose left or right
                        if left_clear and right_clear:
                            direction = np.random.choice([-1, 1])
                        elif left_clear:
                            direction = -1
                        else:
                            direction = 1

                        # Move the grain horizontally
                        int_x += direction
                        x = float(int_x)
                        # Find the top of the pile
                        while check_y > int_y and new_grid[check_y, int_x]:
                            check_y -= 1

                        # Place the grain on top of the pile
                        new_int_y = int(check_y)
                        new_y = float(new_int_y)
                        velocity = 0

            # Update grain position and velocity
            self.sand_grains[i] = [x, new_y, velocity]

            # Mark new position as occupied
            new_grid[int(new_y), int_x] = True

        # Update the grid
        self.grid = new_grid
