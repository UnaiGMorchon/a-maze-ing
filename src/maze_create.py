#!/usr/bin/env python3

from typing import Any
from style import StyleColor

def MazeCreate(config : dict[str, Any]):
    maze: list[list[int]] = []  # todas las filas

    width = config["WIDTH"]
    height = config["HEIGHT"]

    """ # dibujo lineas
    for row in range(height):  # indica la fila que esta dibujando
        print()
        for column in range(width):  # indica la columna
            if row == 0:
                print(StyleColor.nautilus, end="")
            elif row == (height - 1):
                print(StyleColor.nostromo, end="")
            elif column == 0:
                print(StyleColor.magratea, end="")
            elif column == (width -1):
                print(StyleColor.start, end="")
            else:
                print("  ", end="")
            print(maze[row][column], end=" ")  # obtiene el número guardado en esa celda.
    print() """

    # Construye la matriz del laberinto.
    for j in range(height):
        row: list[int] = []  # una fila
        for i in range(width):
            row.append(15)  # creación de celdas a valor 15 todas
        maze.append(row)
    """     maze[3][5] -= 4  # valor 11 abro pared sur
        maze[4][5] -= 1  # valor 14
        maze[3][5] -= 2  # este
        maze[4][5] -= 8  # oeste
    """

    print(maze)

    print("height:", height)
    print("width:", width)
    print("Filas reales:", len(maze))
    print("Columnas primera fila:", len(maze[0]))





""" 

    for j in range(height):
        row: list[int] = []  # una fila
        for i in range(width):
            row.append(15)  # creación de celdas a valor 15 todas
        maze.append(row)
    maze[3][5] -= 4  # valor 11 abro pared sur
    maze[4][5] -= 1  # valor 14
    print(maze)

    

# dibujo lineas
    for row in range(height):  # indica la fila que esta dibujando
        print()
        for column in range(width):  # indica la columna
            if row == 0:
                print(StyleColor.nautilus, end="")
            elif row == (height - 1):
                print(StyleColor.nostromo, end="")
            elif column == 0:
                print(StyleColor.magratea, end="")
            elif column == (width -1):
                print(StyleColor.start, end="")
            else:
                print("  ", end="")
            print(maze[row][column], end=" ")  # obtiene el número guardado en esa celda.
    print()
 """


"""
# dibujo lineas
    for j in range(height):  # indica la fila que esta dibujando
        print()
        for i in range(width):  # indica la columna
            #if j % 2 == 0:
                #print(StyleColor.nautilus, end="")
            #else:
                #print(StyleColor.nostromo, end="")
            print(maze[j][i], end=" ")  # obtiene el número guardado en esa celda.
    print()
"""