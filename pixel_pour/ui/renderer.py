# pixel_pour/ui/renderer.py
import pygame

from pixel_pour.simulation.sand_simulation import SandSimulation


class Renderer:
    """
    A class to separate the rendering process from the main game loop.
    """

    def __init__(self, screen: pygame.Surface):
        """
        Initializes the renderer.
        :param screen: A pygame screen.
        """
        self.screen = screen
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 16)

    def render(self, simulation: SandSimulation, fps: float) -> None:
        """
        Renders the main game loop, each time redrawing the screen and adding the sand grains after.
        :param simulation: An instance of SandSimulation.
        :param fps: A floating point number representing the fps.
        :return: None
        """
        self.screen.fill((0, 0, 0))  # Fill screen with black

        # Convert sand grain positions to integers
        sand_positions = simulation.sand_grains[:, :2].astype(int)

        # Create a surface from the NumPy array
        sand_surface = pygame.Surface(
            (simulation.width, simulation.height), pygame.SRCALPHA
        )
        sand_surface.fill((0, 0, 0, 0))  # Transparent background

        # Draw all sand grains at once
        for x, y in sand_positions:
            pygame.draw.circle(sand_surface, (255, 255, 0), (x, y), 2)

        # Blit the sand surface onto the main screen
        self.screen.blit(sand_surface, (0, 0))

        # Render text for FPS and grain count
        fps_text = self.font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
        grain_count_text = self.font.render(
            f"Grains Poured: {len(simulation.sand_grains)}", True, (255, 255, 255)
        )

        # Blit text onto the screen
        self.screen.blit(fps_text, (10, 10))
        self.screen.blit(grain_count_text, (10, 25))
