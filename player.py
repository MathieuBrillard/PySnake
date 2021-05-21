from numpy import array
from copy import deepcopy
import pygame
import time
import display as d
import genmap as g

class Player:
    """ This class represent a player """
    def __init__(self): # Init the player
        self.alive = True
        self.pos = [[4,8],[3,8],[2,8]]
        self.length = 3
        self.speed = 1
        self.score = 0


    def die(self):
        self.alive = False
        print("Game Over.")

    def move_player(self, carte, key):
        """ This function is for update the player position while a key is pressed """
        old_pos = deepcopy(self.pos)
        #if is_move_legal(self, key) == 1:
            #return
        #else:
        if key in (pygame.K_z,pygame.K_UP): # If "z" is pressed
            if is_something(carte, self.pos[0][0], self.pos[0][1]-1) != 0: # If wall or player
                self.die()
            else:
                carte[self.pos[-1][1], self.pos[-1][0]] = g.abs_map[self.pos[-1][1], self.pos[-1][0]] # Erase old location
                self.pos[0][1] = self.pos[0][1] - 1 # Set the new coords of the head of the snake
                for i in range(len(self.pos)): # Update the position of the body
                    if i != 0:
                        self.pos[i] = old_pos[i-1]
        elif key in (pygame.K_s,pygame.K_DOWN):
            if is_something(carte, self.pos[0][0], self.pos[0][1]+1) != 0:
                self.die()
            else:
                carte[self.pos[-1][1], self.pos[-1][0]] = g.abs_map[self.pos[-1][1], self.pos[-1][0]]
                self.pos[0][1] = self.pos[0][1] + 1
                for i in range(len(self.pos)):
                    if i != 0:
                        self.pos[i] = old_pos[i-1]
        elif key in (pygame.K_q,pygame.K_LEFT):
            if is_something(carte, self.pos[0][0]-1, self.pos[0][1]) != 0:
                self.die()
            else:
                carte[self.pos[-1][1], self.pos[-1][0]] = g.abs_map[self.pos[-1][1], self.pos[-1][0]]
                self.pos[0][0] = self.pos[0][0] - 1
                for i in range(len(self.pos)):
                    if i != 0:
                        self.pos[i] = old_pos[i-1]
        elif key in (pygame.K_d,pygame.K_RIGHT):
            if is_something(carte, self.pos[0][0]+1, self.pos[0][1]) != 0:
                self.die()
            else:
                carte[self.pos[-1][1], self.pos[-1][0]] = g.abs_map[self.pos[-1][1], self.pos[-1][0]]
                self.pos[0][0] = self.pos[0][0] + 1
                for i in range(len(self.pos)): # Update the position of the body
                    if i != 0:
                        self.pos[i] = old_pos[i-1]
        is_bonus(self, carte, key) # Check if there is a bonus and assigne it to the player
        d.print_player(self, carte) # Set the self.pos position on the map


def is_bonus(self, carte, key):
    """
        This function detect if there is an apple and affect it to the player
    """
    if carte[self.pos[0][1],self.pos[0][0]] == 4:
        self.length += 1
        self.score += 1
        if key in (pygame.K_z,pygame.K_UP):
            self.pos.append([self.pos[-1][0],self.pos[-1][1]+1])
        elif key in (pygame.K_s,pygame.K_DOWN):
            self.pos.append([self.pos[-1][0],self.pos[-1][1]-1])
        elif key in (pygame.K_q,pygame.K_LEFT):
            self.pos.append([self.pos[-1][0]+1,self.pos[-1][1]])
        elif key in (pygame.K_d,pygame.K_RIGHT):
            self.pos.append([self.pos[-1][0]-1,self.pos[-1][1]])
        carte = g.gen_apple(carte)


def is_move_legal(self, key):
    """ This function is used to check if a move is legal or not """
    if key in (pygame.K_z,pygame.K_UP):
        if self.pos[0] == [self.pos[1][0],self.pos[1][1]+1]:
            return 1
        else:
            return 0
    elif key in (pygame.K_s,pygame.K_DOWN):
        if self.pos[0] == [self.pos[1][0],self.pos[1][1]-1]:
            return 1
        else:
            return 0
    elif key in (pygame.K_q,pygame.K_LEFT):
        if self.pos[0] == [self.pos[1][0]+1,self.pos[1][1]]:
            return 1
        else:
            return 0
    elif key in (pygame.K_d,pygame.K_RIGHT):
        if self.pos[0] == [self.pos[1][0]-1,self.pos[1][1]]:
            return 1
        else:
            return 0


def continuous_movement(self, carte):
    """ This function is basically a while using a thread to perform a perpetual movement """
    global t_kill
    global touche
    while t_kill == False:
        if touche == None or self.alive == False:
            t_kill = True
        self.move_player(carte, touche)
        time.sleep(0.2111)


def is_something(carte, x_1, y_1):
    """ This function detect if there is something at the specifiate coords """
    wall = 0
    if carte[y_1,x_1] == 0:
        wall = 1
    elif carte[y_1,x_1] == 3:
        wall = 2
    return wall

t_kill = False
touche = None