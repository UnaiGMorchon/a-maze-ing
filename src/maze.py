#!/usr/bin/env python3

from typing import Any
from style import StyleColor

def MazeCreate(config : dict[str, Any]):
    maze: list[list[int]] = []  # todas las filas

    width = config["WIDTH"]
    height = config["HEIGHT"]

    for j in range(height):
        row: list[int] = []  # una fila
        for i in range(width):
            row.append(15)  # creación de celdas a valor 15 todas
        maze.append(row)
    maze[3][5] -= 4
    maze[4][5] -= 1
    print(maze)

# dibujo lineas
    for j in range(height):
        print()
        for i in range(width):
            #if j % 2 == 0:
                #print(StyleColor.nautilus, end="")
            #else:
                #print(StyleColor.nostromo, end="")
            print(maze[j][i], end=" ")
    print()


