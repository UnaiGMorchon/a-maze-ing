#!/usr/bin/env python3

from typing import Any
from src.style import StyleColor

def MazeCreate(config : dict[str, Any]) -> list[list[int]]:
    maze: list[list[int]] = []  # todas las filas

    width = config["WIDTH"]
    height = config["HEIGHT"]

    # Construye la matriz del laberinto.
    for j in range(height):
        row: list[int] = []  # una fila
        for i in range(width):
            row.append(15)  # creación de celdas a valor 15 todas
        maze.append(row)
    return(maze)
