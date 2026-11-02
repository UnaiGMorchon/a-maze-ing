#!/usr/bin/env python3

from typing import Any

def MazeRender(maze: dict[str, Any]):

    # Dibujo del laberinto.

    for row in range(height):  # indica la fila que esta dibujando
        # Dibujamos las paredes NORTE
        
        for column in range(width):  # indica la columna

            print("██", end="")  # 2 caracteres de unión
            # Pared norte
            if maze[row][column] & 1:
                print("██" * 3, end="")  # 6 caracteres
            else:
                print("  " * 3, end="")  # 6 caracteres
        print("██", end="")  # Cierra el extremo derecho y salta de línea
        print()  # Terminamos la línea superior

        for i in range(3):
            # Segunda pasada: paredes verticales e interior
            for column in range(width):
                # dibujamos Pared OESTE
                if maze[row][column] & 8:
                    print("██", end="")
                else:
                    print("  ", end="")

                # Interior de la celda
                # print("  " * 3, end="")
                    # Interior de la celda
                if i == 1:
                    print(f"{maze[row][column]:^6}", end="")
                else:
                    print("  " * 3, end="")

            # Dibujamos Pared ESTE de la última celda
            if maze[row][width -1] & 2:
                print("██", end="")
            else:
                print("  ", end="")
            print()  # terminamos paredes intermedias y centro

    # Dibujamos las paredes SUR
    for column in range(width):
        if maze[height - 1][column] & 4:
            print("██" * 4, end="")
        else:
            print("  " * 4, end="")
    print("██", end="")
    print()
