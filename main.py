import time
import os
import threading
import pygame
import pygame_menu
from pygame.locals import *
import display as d
import genmap as g
import player as p

def paused():
    pause = True
    print("Game Paused")
    time.sleep(1.5)
    while pause:
        pygame.event.clear()
        pygame.event.wait()
        print("Game Unpaused")
        pause = False


def reset():
    g.current_map = g.gen_map(g.current_map)


def save_hi(self):
    ### CREATING TXT FILE ###
    SCRIPT_PATH = os.path.dirname(__file__) #<-- absolute dir the script is in
    REL_PATH = 'data.dump' # name of the output file
    abs_file_path = os.path.join(SCRIPT_PATH, REL_PATH)
    f = open(abs_file_path, "r+") # open the file in read+write
    #########################
    lignes = f.readlines() # put all lignes of the file into a tab
    taille = os.path.getsize(abs_file_path) # get the size of the file
    if taille == 0: # if file is empty
        to_write = 'High Score : {}'.format(self.score)
        f.write(to_write)
        print("High score saved.")
    else:
        f.seek(0) # Go to position 0 in the file
        f.truncate() # empty the file
        for ligne in lignes:
            if "High Score" in ligne:
                hi_score = ligne[13:len(ligne)] # cut the ligne to get only the nb
                if self.score > int(hi_score):
                    to_write = 'High Score : {}'.format(self.score) # set new high score
                    f.write(to_write)
                    print("High score saved.")
                else:
                    to_write = 'High Score : {}'.format(hi_score) # keep old high score
                    f.write(to_write)
                    f.write("")
            else:
                if f.tell() == 0: # if we are at the first line
                    to_write = ligne # do not put a \n
                else:
                    to_write = "\n" + ligne # put a \n
                f.write(to_write)
    f.close()


def grep_hi():
    ### CREATING TXT FILE ###
    SCRIPT_PATH = os.path.dirname(__file__) #<-- absolute dir the script is in
    REL_PATH = 'data.dump' # name of the output file
    abs_file_path = os.path.join(SCRIPT_PATH, REL_PATH)
    f = open(abs_file_path, "r") # open the file in read
    #########################
    taille = os.path.getsize(abs_file_path)
    if taille == 0:
        f.close()
        return None
    else:
        lignes = f.readlines()
        for ligne in lignes:
            if "High Score" in ligne:
                hi_score = ligne
                f.close()
                return hi_score


def game():
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.Font(pygame_menu.font.FONT_NEVIS, 20)
    GAME = True
    # Init players
    player = p.Player()
    print("Player created.")
    # Print the map
    carte = g.current_map
    d.display_map(carte)
    print("Map displayed.")
    # Print Player
    d.print_player(player, carte)
    print("Player displayed.")
    # Generate Apple
    carte = g.gen_apple(carte)
    # Main program
    start = time.time() # Timer
    i = 0
    while GAME:
        score_txt = "Score : {}".format(player.score)
        txt = font.render(score_txt,1,d.white)
        d.dis.blit(txt,(30,455))
        hi_score = grep_hi()
        if hi_score:
            txt2 = font.render(hi_score,1,d.white)
            d.dis.blit(txt2,(370,455))
        pygame.display.update()
        pygame.key.set_repeat(50,50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    GAME = False
                    pygame.quit()
                if event.key in (pygame.K_z,pygame.K_s, pygame.K_q,pygame.K_d,
                    pygame.K_UP,pygame.K_DOWN, pygame.K_LEFT,pygame.K_RIGHT): # Movements
                    if i == 0:
                        p.touche = event.key
                        p.t_kill = False
                        thread = threading.Thread(target=p.continuous_movement, args=(player,carte), daemon=True)
                        thread.start()
                        i = 1
                    else:
                        if p.is_move_legal(player, event.key) == 1:
                            pass
                        else:
                            p.touche = event.key
                if event.key == pygame.K_SPACE: # Pause
                    p.t_kill = True
                    thread.join()
                    i = 0
                    paused()
        if player.alive == False:
            p.t_kill = True
            thread.join()
            GAME = False
            print(score_txt)
            save_hi(player)
            reset()
        d.display_map(carte)

    end = time.time() # End of the timer