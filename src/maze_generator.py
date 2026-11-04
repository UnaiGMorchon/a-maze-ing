#!/usr/bin/env python3

import random
from typing import Any
from src.style import StyleColor


def GeneratorMaze(config: dict[str, Any], maze: list[list[int]]) -> list[tuple[int, int]]:
    """ Generador: utilizado DFS para crear los caminos, eliminando paredes. """
    width = config["WIDTH"]
    height = config["HEIGHT"]
    stack: list[tuple[int, int]] = []  # posiciones guardadas

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

    # 1º list contiene las filas, 2º list contiene los valores de cada fila. int representa los números 0 y 1.
    # Definir el patrón del número 42.
    maze_number_42: list[list[int]] = []
    positions_42: list[tuple[int, int]] = []

    maze_number_42.append([1, 0 ,0, 0, 1, 1, 1])
    maze_number_42.append([1, 0 ,0, 0, 0, 0, 1])
    maze_number_42.append([1, 1, 1, 0, 1, 1, 1])
    maze_number_42.append([0, 0, 1, 0, 1, 0, 0])
    maze_number_42.append([0, 0, 1, 0, 1, 1 ,1])

    # Calcular la posición central del 42.
    start_row = (height - len(maze_number_42)) // 2
    start_column = (width - len(maze_number_42[0])) // 2

    # Reservar las celdas que forman el 42.
    for row1 in range(len(maze_number_42)):
        for column1 in range(len(maze_number_42[0])):
            if maze_number_42[row1][column1] == 1:
                maze_visited[start_row + row1][start_column + column1] = True
                positions_42.append((start_row + row1, start_column + column1))

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
            direction = random.choice(neighbors)  # elige aleatoriamente vecino
            stack.append((row, column))  # guardo posición antes de avanzar
            # Eliminar las paredes entre las dos celdas.
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
            # Retroceder si no quedan vecinos disponibles.
            if len(stack) > 0:
                row, column = stack.pop()  # recupero posicion de stack,elimino de la pila y actuaizo row y column
            else:
                break  # cuando no quedan vecinos ni posiciones pendientes
    # Devolver las posiciones que forman el 42.
    return (positions_42)

