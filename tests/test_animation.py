#!/usr/bin/env python3

import time
import sys
from src.maze_solve import MazeSolve
from src.maze_create import MazeCreate
from src.maze_generator import GeneratorMaze
from a_maze_ing import ReadConfig
from src.maze_render import MazeRender


""" print("Paso 1", flush=True)
time.sleep(0.5)
print("Paso 2", flush=True)
time.sleep(0.5)
print("Paso 3", flush=True)

 """

config = ReadConfig(sys.argv[1])
maze = MazeCreate(config)
pos42 = GeneratorMaze(config, maze, 42)
solve = MazeSolve(config, maze)

for i in range(len(solve)):
    print("\033[H\033[J", end="")
    MazeRender(config, maze, pos42, solve[:i + 1], True)
    time.sleep(0.05)