#!/usr/bin/env python3

from typing import Any

""" solucion con bfs """

def MazeSolve(config: dict[str, Any], maze: list[list[int]]) -> None:
    entry = config["ENTRY"]
    exit = config["EXIT"]
    
    start = (entry[1], entry[0])
    end = (exit[1], exit[0])

    row, column = start

    print("Fila:", row)
    print("Columna:", column)
    print("Paredes:", maze[row][column])

    neighbours: list[tuple[int, int]] = []  # guarda las celdas vecinas accesibles desde una posición
    
    # tuple[int, int]: cada elemento será una tupla con dos enteros, (row, column).
    # set(): crea el conjunto vacío.
    visited : set[tuple[int, int]]= []  # recuerda las celdas ya descubiertas
    visited.add(start)  # hace lo mismo que el append agregar

    # Comprobar si una pared está abierta
    if not (maze[row][column] & 2):
        neighbours.append((row, column + 1))  # Guardar los vecinos accesibles en una lista
        visited.append()
        print("Podemos avanzar hacia el ESTE")

    if not (maze[row][column] & 1):
        neighbours.append((row - 1, column))
        
        print("Podemos avanzar hacia el NORTE")

    if not (maze[row][column] & 4):
        neighbours.append((row + 1, column))
        
        print("Podemos avanzar hacia el SUR")

    if not (maze[row][column] & 8):
        neighbours.append((row, column - 1))
        
        print("Podemos avanzar hacia el OESTE")

    print(neighbours)