from time import sleep
import pygame

# Color data
white = (255, 255, 255)
grey = (60, 60, 60)
#yellow = (255, 255, 102)
black = (0, 0, 0)
red = (240, 26, 40)
#orange = (255, 128, 0)
#brown = (128, 64, 0)
dark_green = (76, 186, 92)
light_green = (26, 240, 57)
#blue = (0, 0, 255)
purple = (162, 76, 186)

# Screen dimensions
DIS_WIDTH = 540
DIS_HEIGHT = 480
# Set the display screen
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake')

def print_player(self, carte):
    """
        This function change the value in the map tab,
        according to the pos of the player.
    """
    for elements in self.pos:
        carte[elements[1], elements[0]] = 3

def display_map(carte):
    """ This function display a map and object on it. """
    colonnes = carte.shape[1] - 1
    lignes = carte.shape[0] - 1
    x_1 = 0
    y_1 = 0
    while y_1 <= lignes:
        while x_1 <= colonnes:
            if carte[y_1,x_1] == 0:
                pygame.draw.rect(dis, grey, [x_1 * 30, y_1 * 30, 30, 30])
            elif carte[y_1,x_1] == 1:
                pygame.draw.rect(dis, dark_green, [x_1 * 30, y_1 * 30, 30, 30])
            elif carte[y_1,x_1] == 2:
                pygame.draw.rect(dis, light_green, [x_1 * 30, y_1 * 30, 30, 30])
            elif carte[y_1,x_1] == 3:
                pygame.draw.rect(dis, purple, [x_1 * 30, y_1 * 30, 30, 30])
                pygame.draw.rect(dis, black, [x_1 * 30, y_1 * 30, 30, 30], 1) # Border
            elif carte[y_1,x_1] == 4:
                pygame.draw.rect(dis, red, [x_1 * 30, y_1 * 30, 30, 30])
            x_1+= 1
        y_1 += 1
        x_1 = 0
