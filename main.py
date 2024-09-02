###########
# MAIN.PY #
###########

import pygame
from pg_utils import *

# Vector2 Setup
vector2 = Vector2()
vector2.init_vectors()

# Vector3 Setup
vector3 = Vector3()
vector3.init_vectors()

# Colors Setup
colors = Color()
colors.init_colors()

# PyGame Setup
pygame.init()

SCREEN = pygame.display.set_mode(RESOLUTION, pygame.FULLSCREEN if FULLSCREEN else 0)
pygame.display.set_caption(WINDOW_NAME)
# pygame.display.set_icon(pygame.image.load(ICON_LOCATION))  # Uncomment if you have an icon

clock = pygame.time.Clock()
delta_time = 0.0

# FUNCTIONS AND CLASSES HERE


def main():
    global delta_time

    running = True
    get_ticks_last_frame = 0.0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        SCREEN.fill(colors.BLACK.get_tup())

        # CODE HERE

        pygame.display.flip()

        get_ticks_last_frame, delta_time = manage_frame_rate(
            clock, get_ticks_last_frame
        )

    pygame.quit()


if __name__ == "__main__":
    main()
