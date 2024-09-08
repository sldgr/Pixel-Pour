# pixel_pour/main.py
import pygame

from pixel_pour.simulation.sand_simulation import SandSimulation
from pixel_pour.ui.renderer import Renderer
from pixel_pour.utils.config import FPS, HEIGHT, SAND_DROP_RATE, WIDTH


def main() -> None:
    """
    Main function running the pygame loop.
    :return: None
    """
    pygame.init()
    pygame.display.set_caption("Pixel Pour")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    simulation = SandSimulation(WIDTH, HEIGHT)
    renderer = Renderer(screen)

    running = True
    mouse_held = False
    sand_drop_counter = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_held = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    mouse_held = False

        if mouse_held:
            sand_drop_counter += 1
            if sand_drop_counter >= SAND_DROP_RATE:
                x, y = pygame.mouse.get_pos()
                simulation.add_sand(x, y)
                sand_drop_counter = 0

        simulation.update()
        fps = clock.get_fps()
        renderer.render(simulation, fps)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
