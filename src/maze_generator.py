#!/usr/bin/env python3

import random
from typing import Any
from src.style import StyleColor
from src.maze_render import MazeRender
from src.maze_pattern import MazePattern
import time


def MazeGenerator(config: dict[str, Any], maze: list[list[int]], seed: int | None = None, maze_animation: bool = False) -> list[tuple[int, int]]:
    """ Generador: utilizado DFS para crear los caminos, eliminando paredes. """
    width = config["WIDTH"]
    height = config["HEIGHT"]
    stack: list[tuple[int, int]] = []  # posiciones guardadas

    rng = random.Random(seed)  # seed la semilla elegimos 42 por defecto siempre saldra el mismo laberinto

    # Crear una matriz para controlar las celdas visitadas.
    maze_visited: list[list[bool]] = []

    # matiz de visita celda true o false
    for row in range(height):
        maze_bool: list[bool] = []  # crea fila vacia
        for column in range(width):  # añado un False por cada columna de la fila actual
            maze_bool.append(False)
        maze_visited.append(maze_bool)  # añades la fila completa a la matriz

    # Marcar la entrada como visitada.
    initial_cor = config["ENTRY"]
    maze_visited[initial_cor[1]][initial_cor[0]] = True
    column = initial_cor[0]
    row = initial_cor[1]

    # Obtener las posiciones del patrón 42.
    positions_42 = MazePattern(config)

    # Marcar las celdas del 42 como visitadas.
    for i in positions_42:
        maze_visited[i[0]][i[1]] = True


    # Explorar celdas mediante DFS.
    while True:
        neighbors: list[str] = []  # lista de vecinos
        # Buscar vecinos dentro del laberinto y no visitados.
        # verificar si estoy dentro del laberinto y guardo sus direcciones
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
            # Elegir un vecino y guardar la posición actual.
            direction = rng.choice(neighbors)  # elige aleatoriamente vecino
            stack.append((row, column))  # guardo posición antes de avanzar
            # Eliminar las paredes entre las dos celdas.
            if direction == "south":
                maze[row][column] -= 4  # quitamos la pared sur
                row += 1  # Bajar una fila.
                maze[row][column] -= 1  # Eliminar la pared norte de la nueva celda.
                maze_visited[row][column] = True  # Marcar la celda como visitada.
            elif direction == "north":
                maze[row][column] -= 1    # quitamos la pared norte
                row -= 1  # Subir una fila.
                maze[row][column] -= 4  # Eliminar la pared sur de la nueva celda.
                maze_visited[row][column] = True
            elif direction == "east":
                maze[row][column] -= 2    # quitamos la pared este
                column += 1  # Avanzar una columna a la derecha.
                maze[row][column] -= 8  # Eliminar la pared oeste de la nueva celda.
                maze_visited[row][column] = True
            elif direction == "west":
                maze[row][column] -= 8    # quitamos la pared oeste
                column -= 1  # Avanzar una columna a la izquierda.
                maze[row][column] -= 2  # Eliminar la pared este de la nueva celda.
                maze_visited[row][column] = True
            # Animacion de crear laberinto
            if maze_animation:
                print("\033[H\033[J", end="")  # limpio teminal
                MazeRender(config, maze, positions_42, "", False)
                time.sleep(0.05)  # lapso de tiempo
        else:
            # Retroceder si no quedan vecinos disponibles.
            if len(stack) > 0:
                row, column = stack.pop()  # recupero posición de stack,elimino de la pila y actuaizo row y column
            else:
                break  # cuando no quedan vecinos ni posiciones pendientes
    count = 0
    for row in maze_visited:
        for i in row:
            if not i:
                count += 1
    #print("Celdas sin visitar:", count)

    if not config["PERFECT"]:
        MazeImperfect(config, maze, positions_42, seed)

    if not config["PERFECT"]:
        MazeImperfect(config, maze, positions_42, seed)

    # Devolver las posiciones que forman el 42.
    return (positions_42)


def MazeImperfect(
        config: dict[str, Any],
        maze: list[list[int]],
        pos_42: list[tuple[int, int]],
        seed: int | None = None
) -> None:
    """Rompe paredes del laberinto"""
    rng: random = random.Random(seed)
    width: int = config["WIDTH"]
    height: int = config["HEIGHT"]
    blocked: set[tuple[int, int]] = set(pos_42)

    # buscamos los dead_ends
    dead_ends: list[tuple[int, int]] = []
    for row in range(height):
        for col in range(width):
            # si no esta dentro del 42
            # y la celda solo tiene una pared abierta, guardamos la posicion
            if (row, col) not in blocked and maze[row][col] in (7, 11, 13, 14):
                dead_ends.append((row, col))

    # buscamos las paredes que se pueden romper
    for cell in dead_ends:
        row, col = cell
        # buscamos las paredes que se pueden romper
        valid_walls: list[tuple[str, tuple[int, int]]] = []
        if maze[row][col] & 1 and row - 1 >= 0 and (row - 1, col) not in blocked:
            valid_walls.append(("north", (row - 1, col)))
        if maze[row][col] & 2 and col + 1 < width and (row, col + 1) not in blocked:
            valid_walls.append(("east", (row, col + 1)))
        if maze[row][col] & 4 and row + 1 < height and (row + 1, col) not in blocked:
            valid_walls.append(("south", (row + 1, col)))
        if maze[row][col] & 8 and col - 1 >= 0 and (row, col - 1) not in blocked:
            valid_walls.append(("west", (row, col - 1)))
        if valid_walls:
            direction, neighbor = rng.choice(valid_walls)
            n_row, n_col = neighbor
            if direction == "north":
                maze[row][col] -= 1
                maze[n_row][n_col] -= 4
            elif direction == "south":
                maze[row][col] -= 4
                maze[n_row][n_col] -= 1
            elif direction == "east":
                maze[row][col] -= 2
                maze[n_row][n_col] -= 8
            elif direction == "west":
                maze[row][col] -= 8
                maze[n_row][n_col] -= 2
