#!/usr/bin/env python3

from typing import Any
from src.style import StyleColor

def MazeRender(config: dict[str, Any], maze: list[list[int]], pos42: list[tuple[int, int]]) -> None:
    width = config["WIDTH"]
    height = config["HEIGHT"]
    entry  = config["ENTRY"]
    exit = config["EXIT"]

    # Dibujo del laberinto.
    for row in range(height):  # indica la fila que esta dibujando
        # Dibujamos las paredes NORTE
        
        for column in range(width):  # indica la columna
            if (row, column) in pos42:
                print(f"{StyleColor.number_42}{"██"}{StyleColor.reset}", end="")
            else:
                print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")  # 2 caracteres de unión

            # Pared norte
            if (row, column) in pos42:
                print(f"{StyleColor.number_42}{"██"* 1}{StyleColor.reset}", end="")
            elif maze[row][column] & 1:
                print(f"{StyleColor.wall}{"██" * 1}{StyleColor.reset}", end="")  # 6 caracteres
            else:
                print(f"{StyleColor.background}{"  " * 1}{StyleColor.reset}", end="")  # 6 caracteres
        print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")  # Cierra el extremo derecho y salta de línea
        print()  # Terminamos la línea superior

        for i in range(1):
            # Segunda pasada: paredes verticales e interior
            for column in range(width):

                # dibujamos Pared OESTE
                if (row, column) in pos42:
                    print(f"{StyleColor.number_42}{"██"}{StyleColor.reset}", end="")
                elif maze[row][column] & 8:
                    print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")
                else:
                    print(f"{StyleColor.background}{"  "}{StyleColor.reset}", end="")

                # Interior de la celda
                if (column , row) ==  exit:
                    print(f"{StyleColor.red}{"██" * 1}{StyleColor.reset}", end="")
                elif (column, row) == entry:
                    print(f"{StyleColor.green}{"██" * 1}{StyleColor.reset}", end="")
                elif (row, column) in pos42:
                    print(f"{StyleColor.number_42}{"██" * 1}{StyleColor.reset}", end="")
                elif i == 0:
                    print(f"{StyleColor.background}{maze[row][column]:^2}{StyleColor.reset}", end="")
                else:
                    print(f"{StyleColor.background}{"  " * 1}{StyleColor.reset}", end="")

            # Dibujamos Pared ESTE de la última celda
            if maze[row][width -1] & 2:
                print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")
            else:
                print(f"{StyleColor.background}{"  "}{StyleColor.reset}", end="")
            print()  # terminamos paredes intermedias y centro

    # Dibujamos las paredes SUR
    for column in range(width):
        if maze[height - 1][column] & 4:
            print(f"{StyleColor.wall}{"██" * 2}{StyleColor.reset}", end="")
        else:
            print(f"{StyleColor.background}{"  " * 2}{StyleColor.reset}", end="")
    print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")
    print()