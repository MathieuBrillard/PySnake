import numpy
from copy import deepcopy
from random import randint

def gen_map(carte):
    """ This function is used to generate the tab of the map """
    colonnes = carte.shape[1] - 1
    lignes = carte.shape[0] - 1
    x_1 = 0
    y_1 = 0
    while y_1 <= lignes: # Define upper and lower sides borders map
        if y_1 == 0 or y_1 == lignes:
            while x_1 <= colonnes:
                carte[y_1,x_1] = 0
                x_1 += 1
        else:
            while x_1 <= colonnes:
                if x_1 == 0 or x_1 == colonnes: # Define sides borders map
                    carte[y_1,x_1] = 0
                else:
                    if y_1 % 2 == 0:
                        if x_1 % 2 == 0:
                            carte[y_1,x_1] = 2
                        else:
                            carte[y_1,x_1] = 1
                    else:
                        if x_1 % 2 == 0:
                            carte[y_1,x_1] = 1
                        else:
                            carte[y_1,x_1] = 2
                x_1 += 1
        y_1 += 1
        x_1 = 0
    return carte

def gen_apple(carte):
    """ This function is used to generate apples on the map """
    possible = []
    y = 0
    i = 0
    while y < len(carte):
        while i < len(carte[y]):
            if carte[y][i] == 1 or carte[y][i] == 2:
                possible.append([i, y])
            i+=1
        i = 0
        y+=1
    x = randint(0, len(possible)-1)
    apple = possible[x]
    carte[apple[1],apple[0]] = 4
    return carte


current_map = numpy.array(numpy.zeros(shape=[16,18],dtype=int)) # Size
current_map = gen_map(current_map) # Generation
abs_map = deepcopy(current_map)
print("Map generated")