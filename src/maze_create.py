#!/usr/bin/env python3

from typing import Any
from src.style import StyleColor

def MazeCreate(config : dict[str, Any]) -> list[list[int]]:
    """Crea una matriz con todas las paredes cerradas."""
    maze: list[list[int]] = []  # todas las filas

    width = config["WIDTH"]
    height = config["HEIGHT"]

    # Construye la matriz del laberinto filas.
    for j in range(height):
        row: list[int] = []  # una fila
        # Añadir celdas con las cuatro paredes cerradas.
        for i in range(width):
            row.append(15)  # creación de celdas a valor 15 todas
        # Añadir la fila completa a la matriz.
        maze.append(row)
    return(maze)
