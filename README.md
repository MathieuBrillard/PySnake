# PySnake
## a basic snake game in python

This game is a *copy of the well know **Snake game***, which was developped in the purpose of *learning about Object Oriented programmation with **Python***.

---

## Installation

First of all, you need to have [python] v3.9.7 installed (everything might work with higher version, but it has never been tested).

You can install the packages needed by executing this command:
```
python -m pip install -r .\requirements.txt
```
You have to possibility to build an exe for this game, using:
```
python .\setup.py --quiet build
```
But it's not working at the moment, because of the way High Scores are saved.
So, instead, to actually play you can use:
```
python .\menu.py
```

---

## Development

You can get the lastest version of the game on the following [repository].

Currently, the game is working but not everything is finished:
* Available :
    * There is a High Score system, so you can keep track of your records.
* Not available at the moment:
    * Change the difficulty (snake is moving faster)
    * Change the color of the snake
    * Online/Offline scoreboard
    * Building the executable (crashing when loading the game)


[//]: # (Links)

   [python]: <https://www.python.org/downloads/>
   [repository]: <https://github.com/MathieuBrillard/PySnake>