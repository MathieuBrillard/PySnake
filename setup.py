import os
from cx_Freeze import setup, Executable

base = None    

SCRIPT_PATH = os.path.dirname(__file__) #<-- absolute dir the script is in
REL_PATH = 'menu.py'
abs_file_path = os.path.join(SCRIPT_PATH, REL_PATH)

executables = [Executable(abs_file_path, base=base)]

packages = ["pygame", "time", "threading", "numpy", "copy", "random", "pygame_menu"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Snake",
    options = options,
    version = "1.1",
    description = 'Snake Game',
    executables = executables
)