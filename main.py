import time
import threading
import pygame
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


pygame.init()
font = pygame.font.Font(None, 25)
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
    d.dis.blit(txt,(30,458))
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
        pygame.quit()
    d.display_map(carte)

end = time.time() # End of the timer