#!/usr/bin/env python3

from typing import Any
from src.style import StyleColor

def MazeRender(config: dict[str, Any], maze: list[list[int]], pos42: list[tuple[int, int]], solve: str) -> None:
    """Dibuja el laberinto y su solución en la terminal."""
    width = config["WIDTH"]
    height = config["HEIGHT"]
    entry  = config["ENTRY"]
    exit = config["EXIT"]

    # Convertir los movimientos de la solución(solve (ESNWSENW)) en coordenadas.
    # Celdas que forman el camino.
    draw_line: list[tuple[int, int]] = [(entry[1], entry[0])]
    draw_north: list[tuple[int, int]] = []  # Pasos verticales entre celdas.
    draw_west: list[tuple[int, int]] = []  # Pasos horizontales entre celdas.
    
    row, column = draw_line[0]  # Obtener las coordenadas iniciales.
    # Recorrer los movimientos de la solución.
    for i in solve:
        # Avanzar hacia el norte.
        if i == "N":
            row -= 1  # Subir una fila.
            draw_line.append((row, column))  # Guardar la nueva posición.
            draw_north.append((row + 1, column))  # Abertura norte de la celda anterior.
        # Avanzar hacia el sur.
        if i == "S":
            row +=1   # Bajar una fila.
            draw_line.append((row, column))
            draw_north.append((row, column))  # Abertura norte de la celda actual.
        # Avanzar hacia el este.
        if i == "E":
            column += 1  # Mover una columna a la derecha.
            draw_line.append((row, column))
            draw_west.append((row, column))  # Abertura oeste de la celda actual.
        # Avanzar hacia el oeste.
        if i == "W":
            column -=1  # Mover una columna a la izquierda.
            draw_line.append((row, column))
            draw_west.append((row, column + 1))  # Abertura oeste de la celda anterior.

    # Recorrer las filas del laberinto.
    # Dibujo del laberinto.
    for row in range(height):  # indica la fila que esta dibujando

        # Dibujamos las paredes NORTE
        for column in range(width):  # indica la columna
            if (row, column) in pos42:
                print(f"{StyleColor.number_42}{"██"}{StyleColor.reset}", end="")
            else:
                print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")  # 2 caracteres de unión

            # Dibujar la pared o el paso NORTE.
            if (row, column) in pos42:
                print(f"{StyleColor.number_42}{"██"* 1}{StyleColor.reset}", end="")
            elif maze[row][column] & 1:
                print(f"{StyleColor.wall}{"██" * 1}{StyleColor.reset}", end="")  # 6 caracteres
            # Pintar los pasos verticales de la solución.
            elif (row, column) in draw_north:
                print(f"{StyleColor.solve}{"██"}{StyleColor.reset}", end="")
            else:
                print(f"{StyleColor.background}{"  " * 1}{StyleColor.reset}", end="")  # 6 caracteres
        # Cierra el extremo derecho y salta de línea
        print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")
        print()  # Terminamos la línea superior

        # Dibujar paredes oeste e interiores
        for i in range(1):
            # Segunda pasada: paredes verticales e interior
            for column in range(width):

                # Dibujar la pared o el paso OESTE.
                if (row, column) in pos42:
                    print(f"{StyleColor.number_42}{"██"}{StyleColor.reset}", end="")
                elif maze[row][column] & 8:
                    print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")
                # Pintar los pasos horizontales de la solución.
                elif (row, column) in draw_west:
                    print(f"{StyleColor.solve}{"██"}{StyleColor.reset}", end="")
                else:
                    print(f"{StyleColor.background}{"  "}{StyleColor.reset}", end="")

                # Dibujar el interior de cada celda.
                if (column , row) ==  exit:
                    print(f"{StyleColor.red}{"██" * 1}{StyleColor.reset}", end="")
                elif (column, row) == entry:
                    print(f"{StyleColor.green}{"██" * 1}{StyleColor.reset}", end="")
                elif (row, column) in pos42:
                    print(f"{StyleColor.number_42}{"██" * 1}{StyleColor.reset}", end="")
                # dibujo de la linea
                elif (row, column) in draw_line:
                    print(f"{StyleColor.solve}{"██"}{StyleColor.reset}", end="")
                #elif i == 0:
                #    print(f"{StyleColor.background}{maze[row][column]:^2}{StyleColor.reset}", end="")
                else:
                    print(f"{StyleColor.background}{"  " * 1}{StyleColor.reset}", end="")

            # Dibujamos Pared ESTE de la última celda del laberinto.
            if maze[row][width -1] & 2:
                print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")
            else:
                print(f"{StyleColor.background}{"  "}{StyleColor.reset}", end="")
            print()  # terminamos paredes intermedias y centro

    # Dibujamos las paredes SUR del laberinto
    for column in range(width):
        if maze[height - 1][column] & 4:
            print(f"{StyleColor.wall}{"██" * 2}{StyleColor.reset}", end="")
        else:
            print(f"{StyleColor.background}{"  " * 2}{StyleColor.reset}", end="")
    print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")
    print()