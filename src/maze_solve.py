#!/usr/bin/env python3

from typing import Any


def MazeSolve(config: dict[str, Any], maze: list[list[int]]) -> str:
    """Busca el camino más corto con el algoritmo BFS. (FIFO (First In, First Out))"""
    entry = config["ENTRY"]
    exit = config["EXIT"]

    # Convertir coordenadas (y, x) a (fila, columna).
    start = (entry[1], entry[0])
    end = (exit[1], exit[0])

    row, column = start

    #print("Fila:", row)
    #print("Columna:", column)
    #print("Paredes:", maze[row][column])

    # El proceso será:
    # 1. Sacar una posición de queue.
    # 2. Obtener su fila y columna.
    # 3. Comprobar sus cuatro paredes.
    # 4. Descubrir sus vecinos.

    # Cola de posiciones pendientes y caminos recorridos.
    queue: list[tuple[tuple[int, int], str]] = [(start, "")]  # cola con la posición inicial (start) first in, first out bfs
    # Celdas ya descubiertas
    visited : list[tuple[int, int]]= []  # recuerda las celdas ya descubiertas
    visited.append(start)  # append agregar la primera posición
 
    while queue:
        # Cada celda tiene sus propios vecinos
        neighbours: list[tuple[tuple[int, int], str]] = []  # guarda las celdas vecinas accesibles desde una posición
        # Extraer la primera posición de la cola (FIFO).
        current = queue.pop(0)  # sacamos la primeras coordenadas
        position, path = current  # las desenpaquetamos
        row, column = position

        """ print("CURRENT:", current)
        print("ROW:", row, type(row))
        print("COLUMN:", column, type(column)) """

        # Devolver el camino al llegar a la salida.
        if position == end:  # si es igual a end
            print("Camino encontrado:", path)
            print("Número de movimientos:", len(path))
            return (path)

        # Comprobar si una pared está abierta y guardamos vecinos
        if not (maze[row][column] & 2):  # Guarda las coordenadas del vecino y la dirección.
            neighbours.append(((row, column + 1), "E"))  # Guardar las coordenadas de los vecinos a los que podemos avanzar + E.
            #print("Podemos avanzar hacia el ESTE")

        if not (maze[row][column] & 1):
            neighbours.append(((row - 1, column), "N"))
            #print("Podemos avanzar hacia el NORTE")

        if not (maze[row][column] & 4):
            neighbours.append(((row + 1, column), "S"))
            #print("Podemos avanzar hacia el SUR")

        if not (maze[row][column] & 8):
            neighbours.append(((row, column - 1), "W"))
            #print("Podemos avanzar hacia el OESTE")

        # Añadir a la cola los vecinos no visitados.
        for neighbour, direction in neighbours:  # recorrer los vecinos encontrados, direcciones
            if neighbour not in visited:  # ¿Este vecino todavía no está en la lista? añade solo los no visitados
                visited.append(neighbour)  # Marcar el vecino como descubierto.
                queue.append((neighbour, path + direction))  # Guardar el vecino y su camino para explorarlo después.

    # No existe un camino hasta la salida.
    raise ValueError("No se ha encontrado un camino hasta la salida")
