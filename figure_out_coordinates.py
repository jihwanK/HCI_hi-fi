import pygame
import sys
import math


pygame.init()

## ---- CONSTANTS ---- ##

# RESOLUTION
WIDTH = 960
HEIGHT = 720

# COLORS
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

## ------------------- ##

class Launchpad:

    def __init__(self):
        self.total = 18
        self.main_center = WIDTH // 2
        self.icon_width = 60
        self.app = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    def display_launchpad(self):

        num_of_col = 5
        num_of_row = math.ceil(self.total / num_of_col)

        i = 0
        j = 0
        for k in range(len(self.app)):
            if i == num_of_row:
                i = 0
            if j == num_of_col:
                j = 0
                i += 1
            center = 96 * (j * 1 * 2) + 96
            x_pos = center - (self.icon_width // 2)
            y_pos = 80 + (130 * i)
            pygame.draw.rect(screen, BLACK, [x_pos, y_pos, self.icon_width, self.icon_width], 2)
            j += 1





class Dock:

    def __init__(self):
        self.total = 6
        self.padding = 15
        self.main_center = WIDTH // 2
        self.icon_width = 45
        self.app = [4, 5, 6, 7, 8, 9]
        self.dock_y_position = 630

    def display_dock(self):

        # display dock container
        dock_container_size = (self.total * self.icon_width) + (self.padding * 2 * self.total)
        dock_container_x_pos = self.main_center - (dock_container_size // 2)
        dock_container_y_pos = self.dock_y_position
        dock_container_height = 75
        pygame.draw.rect(screen, BLACK, [dock_container_x_pos, dock_container_y_pos, dock_container_size, dock_container_height], 2)

        for i in range(len(self.app)):
            center = 37.5 * (i * 2 + 1) + dock_container_x_pos
            x_pos = center - (self.icon_width // 2)
            y_pos = self.dock_y_position + 10
            pygame.draw.rect(screen, BLACK, [x_pos, y_pos, self.icon_width, self.icon_width], 2)

size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example ipad interface")

dock = Dock()
launchpad = Launchpad()

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(WHITE)

    dock.display_dock()
    launchpad.display_launchpad()

    pygame.display.flip()


pygame.quit()
