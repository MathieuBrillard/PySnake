import os
import pygame
from pygame.event import wait
import pygame_menu
import main as m

from typing import Tuple, Optional

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

# -----------------------------------------------------------------------------
# Constants and global variables
# -----------------------------------------------------------------------------
FPS = 60
WINDOW_SIZE = (540, 480)

surface: Optional['pygame.Surface'] = None
main_menu: Optional['pygame_menu.Menu'] = None

# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------
def main_background() -> None:
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.
    :return: None
    """
    surface.fill((40, 40, 40))


def check_name_test(value: str) -> None:
    """
    This function tests the text input widget.
    :param value: The widget value
    :return: None
    """
    print('User name: {0}'.format(value))


def main(test: bool = False) -> None:
    """
    Main program.
    :param test: Indicate function is being tested
    :return: None
    """

    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global main_menu
    global surface

    # -------------------------------------------------------------------------
    # Create window
    # -------------------------------------------------------------------------
    #surface = create_example_window('Example - Multi Input', WINDOW_SIZE)
    pygame.init()
    surface = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Create menus: Settings
    # -------------------------------------------------------------------------
    settings_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    settings_menu_theme.title_offset = (5, -2)
    settings_menu_theme.title_font = pygame_menu.font.FONT_NEVIS
    settings_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    settings_menu_theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT
    settings_menu_theme.widget_font = pygame_menu.font.FONT_NEVIS
    settings_menu_theme.widget_font_size = 20

    settings_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        theme=settings_menu_theme,
        title='Settings',
        width=WINDOW_SIZE[0]
    )

    # Add text inputs with different configurations
    settings_menu.add.text_input(
        'Name : ',
        default='PlayerName',
        maxchar=15,
        onreturn=check_name_test,
        textinput_id='name'
    )

    # Selectable items
    items = [('Normal', 'NORMAL'),
             ('Hard', 'HARD'),
             ('Extreme', 'EXTREME')]
    
    # Difficulty options selector
    settings_menu.add.selector(
        'Select difficulty',
        items,
        selector_id='difficulty',
        default=0,
        style='fancy'
    )

    settings_menu.add.dropselect_multiple(
        title='Choose a color :',
        items=[('Black', (0, 0, 0)),
               ('Blue', (0, 0, 255)),
               ('Cyan', (0, 255, 255)),
               ('Fuchsia', (255, 0, 255)),
               ('Green', (0, 255, 0)),
               ('Red', (255, 0, 0)),
               ('White', (255, 255, 255)),
               ('Yellow', (255, 255, 0))],
        dropselect_multiple_id='pickcolors',
        max_selected=1,
        open_middle=True,
        selection_box_height=6  # How many options show if opened
    )

    settings_menu.add.color_input(
        'Or, make your own color : ',
        color_type='rgb',
        color_id='color',
        default=(255, 0, 0),
        input_separator=','
    )

    def data_store() -> None:
        """
        Save data of the menu.
        :return: None
        """
        SCRIPT_PATH = os.path.dirname(__file__) #<-- absolute dir the script is in
        REL_PATH = 'data.dump' # name of the output file
        abs_file_path = os.path.join(SCRIPT_PATH, REL_PATH)
        f = open(abs_file_path, "r+") # open the file in read+write
        lignes = f.readlines() # put all lignes of the file into a tab
        taille = os.path.getsize(abs_file_path) # get the size of the file
        data = settings_menu.get_input_data()
        to_save = []

        for k in data.keys():
            to_write = u'{0} : {1}'.format(k, data[k])
            to_save.append([to_write])
        if taille == 0: # if file is empty
            for line in to_save:
                if f.tell() == 0:
                    f.write("Settings :")
                to_write = "\n" + line
                f.write(to_write)
            f.write("\n---")
            print("Settings saved.")
        else:
            f.seek(0) # Go to position 0 in the file
            f.truncate() # empty the file
            i = 0
            while i < len(lignes):
                if "Settings :" in lignes[i]:
                    f.write(lignes[i])
                    i += 1
                    while lignes[i] != "---":
                        f.write()
                else:
                    if f.tell() == 0: # if we are at the first line
                        to_write = lignes[i] # do not put a \n
                    else:
                        to_write = "\n" + lignes[i] # put a \n
                    f.write(to_write)
                i += 1
        f.close()


    settings_menu.add.button('Store data', data_store, button_id='store')  # Call function
    settings_menu.add.button('Restore original values', settings_menu.reset_value)
    settings_menu.add.button('Return to main menu', pygame_menu.events.BACK,
                             align=pygame_menu.locals.ALIGN_CENTER)

    # -------------------------------------------------------------------------
    # Create menus: Main menu
    # -------------------------------------------------------------------------
    main_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    main_menu_theme.title_font = pygame_menu.font.FONT_NEVIS
    main_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    main_menu_theme.widget_font = pygame_menu.font.FONT_NEVIS
    main_menu_theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
    main_menu_theme.widget_font_size = 30

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        theme=main_menu_theme,
        title='Main menu',
        width=WINDOW_SIZE[0]
    )
    #if grep_hi() != None:
    #    to_print = grep_hi()
    #    main_menu.add.label(to_print)
    main_menu.add.button('Start Game', m.game, button_id='game')
    main_menu.add.button('Settings', settings_menu)
    main_menu.add.button('Exit', pygame_menu.events.EXIT)

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Main menu
        main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break

if __name__ == '__main__':
    main()