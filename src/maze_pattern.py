#!/usr/bin/env python3

from typing import Any


def MazePattern(config: dict[str, Any]) -> list[tuple[int, int]]:
    width = config["WIDTH"]
    height = config["HEIGHT"]

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

    if height < len(maze_number_42) or width < 9:
        print("42 doesn't fit, so generate the maze without that pattern.")
    else:
        # Reservar las celdas que forman el 42.
        for row1 in range(len(maze_number_42)):
            # Recorrer las columnas de cada fila.
            for column1 in range(len(maze_number_42[0])):
                # Comprobar si la celda forma parte del 42.
                if maze_number_42[row1][column1] == 1:
                    # Guardar las coordenadas del 42 dentro del laberinto.
                    positions_42.append((start_row + row1, start_column + column1))
    return positions_42