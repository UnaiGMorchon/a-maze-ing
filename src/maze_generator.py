#!/usr/bin/env python3

import random
from typing import Any

def GeneratorMaze(config: dict[str, Any], maze: list[list[int]]) -> None:
    width = config["WIDTH"]
    height = config["HEIGHT"]
    stack: list[tuple[int, int]] = []  # posiciones guardadas

    maze_visited: list[list[bool]] = []

    # matiz de visita celda true o false
    for row in range(height):
        maze_bool: list[bool] = []  # crea fila vacia
        for column in range(width):  # añado un False por cada columna de la fila actual
            maze_bool.append(False)
        maze_visited.append(maze_bool)  # añades la fila completa a la matriz

    initial_cor = config["ENTRY"]
    maze_visited[initial_cor[1]][initial_cor[0]] = True
    column = initial_cor[0]
    row = initial_cor[1]

    while True:
        neighbors: list[str] = []  # lista de vecinos
        # verificar si enstoy dentro del laberinto y guardo sus direcciones
        if row < height -1 and not maze_visited[row + 1][column]:  # sur
            neighbors.append("south")  # guardo el sentido sur

        if row > 0 and not maze_visited[row - 1][column]:  # norte
            neighbors.append("north")  # guardo el sentido norte

        if column < width -1 and not maze_visited[row][column + 1]:  # este
            neighbors.append("east")  # guardo el sentido este

        if column > 0 and not maze_visited[row][column - 1]:  # oeste
            neighbors.append("west")  # guardo el sentido oeste

        
        # lista de vecinos disponibles neighbors
        if len(neighbors) > 0:  # que tenga al menos 1
            direction = random.choice(neighbors)  # elige aleatoriamente vecino
            stack.append((row, column))  # guardo posición antes de avanzar
            if direction == "south":
                maze[row][column] -= 4
                row += 1
                maze[row][column] -= 1
                maze_visited[row][column] = True
            elif direction == "north":
                maze[row][column] -= 1
                row -= 1
                maze[row][column] -= 4
                maze_visited[row][column] = True
            elif direction == "east":
                maze[row][column] -= 2
                column += 1
                maze[row][column] -= 8
                maze_visited[row][column] = True
            elif direction == "west":
                maze[row][column] -= 8
                column -= 1
                maze[row][column] -= 2
                maze_visited[row][column] = True
        else:
            if len(stack) > 0:
                row, column = stack.pop()  # recupero posicion de stack,elimino de la pila y actuaizo row y column
            else:
                break  # cuando no quedan vecinos ni posiciones pendientes


