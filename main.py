import pygame
from pygame.locals import *
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RESOLUTION = 50
LINE_THICKNESS = 3
BOTTOM_COLOR = (0, 50, 125)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Function to calculate the Bezier curve
def bezier_curve(t, points):
    B = [(1 - t) ** 2, 2 * (1 - t) * t, t ** 2]
    return tuple(sum(B[i] * points[i][j] for i in range(3)) for j in range(2))


# Control points for the Bezier curve
control_points = [(100, 100),
                  (300, 200),
                  (500, 100)]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Calculate all points of the Bezier curve
    curve_points = [bezier_curve(t / RESOLUTION, control_points) for t in range(0, RESOLUTION + 1)]

    # Draw polygon between control points and curve points
    pygame.draw.polygon(screen, BOTTOM_COLOR, curve_points)

    # Initialize the previous point
    prev_point = None

    # Draw the Bezier curve
    for point in curve_points:
        current_point = (int(point[0]), int(point[1]))
        if prev_point is not None:
            pygame.draw.line(screen, BLACK, prev_point, current_point, LINE_THICKNESS)
        prev_point = current_point

    # Update the display
    pygame.display.flip()