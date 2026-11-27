from typing import Any
import random
import time
from mazegen.maze_validate import MazeConfigError
from mazegen.style import StyleColor
from .pattern42 import pattern42


class MazeGenerator:

    def __init__(
            self,
            width: int,
            height: int,
            entry: tuple[int, int],
            exit: tuple[int, int],
            op_file: str = "maze.txt",
            is_perfect: bool = True,
            seed: int | None = None,
            algorithm: str | None = None,
            grid: list[list[int]] = [],
            solution: str = None
    ) -> None:
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.op_file = op_file
        self.is_perfect = is_perfect
        self.seed = seed
        self.algorithm = algorithm
        self.grid = grid
        self.solution = solution

    def maze_create(self) -> None:
        """Crea una matriz con todas las paredes cerradas."""
        maze: list[list[int]] = []  # todas las filas
        # Construye la matriz del laberinto filas.
        for _ in range(self.height):
            row: list[int] = []  # una fila
            # Añadir celdas con las cuatro paredes cerradas.
            for _ in range(self.width):
                row.append(15)  # creación de celdas a valor 15 todas
            # Añadir la fila completa a la matriz.
            maze.append(row)
        self.grid = maze

    def maze_paths(
            self, maze_animation: bool = False
    ) -> list[tuple[int, int]]:
        """ Generador: utilizado DFS para crear los caminos, eliminando paredes. """
        stack: list[tuple[int, int]] = []  # posiciones guardadas

        rng = random.Random(self.seed)  # seed la semilla elegimos 42 por defecto siempre saldra el mismo laberinto

        # Crear una matriz para controlar las celdas visitadas.
        maze_visited: list[list[bool]] = []

        # matiz de visita celda true o false
        for row in range(self.height):
            maze_bool: list[bool] = []  # crea fila vacia
            for column in range(self.width):  # añado un False por cada columna de la fila actual
                maze_bool.append(False)
            maze_visited.append(maze_bool)  # añades la fila completa a la matriz

        # Marcar la entrada como visitada.
        initial_cor = self.entry
        maze_visited[initial_cor[1]][initial_cor[0]] = True
        column = initial_cor[0]
        row = initial_cor[1]

        # Obtener las posiciones del patrón 42.
        config = {"WIDTH": self.width, "HEIGHT": self.height}
        positions_42 = pattern42(config)

        # Marcar las celdas del 42 como visitadas.
        for i in positions_42:
            maze_visited[i[0]][i[1]] = True

        # Explorar celdas mediante DFS.
        while True:
            neighbors: list[str] = []  # lista de vecinos
            # Buscar vecinos dentro del laberinto y no visitados.
            # verificar si estoy dentro del laberinto y guardo sus direcciones
            if row < self.height - 1 and not maze_visited[row + 1][column]:  # sur
                neighbors.append("south")  # guardo el sentido sur

            if row > 0 and not maze_visited[row - 1][column]:  # norte
                neighbors.append("north")  # guardo el sentido norte

            if column < self.width - 1 and not maze_visited[row][column + 1]:  # este
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
                    self.grid[row][column] -= 4  # quitamos la pared sur
                    row += 1  # Bajar una fila.
                    self.grid[row][column] -= 1  # Eliminar la pared norte de la nueva celda.
                    maze_visited[row][column] = True  # Marcar la celda como visitada.
                elif direction == "north":
                    self.grid[row][column] -= 1    # quitamos la pared norte
                    row -= 1  # Subir una fila.
                    self.grid[row][column] -= 4  # Eliminar la pared sur de la nueva celda.
                    maze_visited[row][column] = True
                elif direction == "east":
                    self.grid[row][column] -= 2    # quitamos la pared este
                    column += 1  # Avanzar una columna a la derecha.
                    self.grid[row][column] -= 8  # Eliminar la pared oeste de la nueva celda.
                    maze_visited[row][column] = True
                elif direction == "west":
                    self.grid[row][column] -= 8    # quitamos la pared oeste
                    column -= 1  # Avanzar una columna a la izquierda.
                    self.grid[row][column] -= 2  # Eliminar la pared este de la nueva celda.
                    maze_visited[row][column] = True
                # Animacion de crear laberinto
                if maze_animation:
                    print("\033[H\033[J", end="")  # limpio teminal
                    self.maze_render(positions_42, "", False)
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

        if not self.is_perfect:
            self.make_imperfect(
                config, self.grid, positions_42,
                maze_animation, self.seed
                )

        # Devolver las posiciones que forman el 42.
        return (positions_42)

    def make_imperfect(
        self,
        config: dict[str, Any],
        grid: list[list[int]],
        pos_42: list[tuple[int, int]],
        maze_animation: bool = False,
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
                if (row, col) not in blocked and grid[row][col] in (7, 11, 13, 14):
                    dead_ends.append((row, col))

        # buscamos las paredes que se pueden romper
        for cell in dead_ends:
            row, col = cell
            # buscamos las paredes que se pueden romper
            valid_walls: list[tuple[str, tuple[int, int]]] = []
            if grid[row][col] & 1 and row - 1 >= 0 and (row - 1, col) not in blocked:
                valid_walls.append(("north", (row - 1, col)))
            if grid[row][col] & 2 and col + 1 < width and (row, col + 1) not in blocked:
                valid_walls.append(("east", (row, col + 1)))
            if grid[row][col] & 4 and row + 1 < height and (row + 1, col) not in blocked:
                valid_walls.append(("south", (row + 1, col)))
            if grid[row][col] & 8 and col - 1 >= 0 and (row, col - 1) not in blocked:
                valid_walls.append(("west", (row, col - 1)))
            # quitamos las paredes
            if valid_walls:
                direction, neighbor = rng.choice(valid_walls)
                n_row, n_col = neighbor
                if direction == "north":
                    grid[row][col] -= 1
                    grid[n_row][n_col] -= 4
                elif direction == "south":
                    grid[row][col] -= 4
                    grid[n_row][n_col] -= 1
                elif direction == "east":
                    grid[row][col] -= 2
                    grid[n_row][n_col] -= 8
                elif direction == "west":
                    grid[row][col] -= 8
                    grid[n_row][n_col] -= 2
                if maze_animation:
                    print("\033[H\033[J", end="")  # limpio teminal
                    self.maze_render(pos_42, "", False)
                    time.sleep(0.05)  # lapso de tiempo

    def maze_solve(self) -> str:
        """Busca el camino más corto con el algoritmo BFS. (FIFO (First In, First Out))"""

        # Convertir coordenadas (y, x) a (fila, columna).
        start = (self.entry[1], self.entry[0])
        end = (self.exit[1], self.exit[0])

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
        visited: list[tuple[int, int]] = []  # recuerda las celdas ya descubiertas
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
                #print("Camino encontrado:", path)
                #print("Número de movimientos:", len(path))
                return (path)

            # Comprobar si una pared está abierta y guardamos vecinos
            if not (self.grid[row][column] & 2):  # Guarda las coordenadas del vecino y la dirección.
                if column < self.width - 1:
                    neighbours.append(((row, column + 1), "E"))  # Guardar las coordenadas de los vecinos a los que podemos avanzar + E.
                #print("Podemos avanzar hacia el ESTE")

            if not (self.grid[row][column] & 1):
                if row > 0:
                    neighbours.append(((row - 1, column), "N"))
                    #print("Podemos avanzar hacia el NORTE")

            if not (self.grid[row][column] & 4):
                if row < self.height - 1:
                    neighbours.append(((row + 1, column), "S"))
                    #print("Podemos avanzar hacia el SUR")

            if not (self.grid[row][column] & 8):
                if column > 0:
                    neighbours.append(((row, column - 1), "W"))
                    #print("Podemos avanzar hacia el OESTE")

            # Añadir a la cola los vecinos no visitados.
            for neighbour, direction in neighbours:  # recorrer los vecinos encontrados, direcciones
                if neighbour not in visited:  # ¿Este vecino todavía no está en la lista? añade solo los no visitados
                    visited.append(neighbour)  # Marcar el vecino como descubierto.
                    queue.append((neighbour, path + direction))  # Guardar el vecino y su camino para explorarlo después.

        # No existe un camino hasta la salida.
        raise ValueError("No se ha encontrado un camino hasta la salida")

    def maze_save(self) -> None:
        """Guarda el laberinto y su solución en un archivo."""
        self.solution = self.maze_solve()
        try:
            # Abrir el archivo en modo escritura.
            with open(self.op_file, "w", encoding="utf-8") as file:
                # Guardar cada fila del laberinto en hexadecimal.
                for row in self.grid:
                    for i in row:
                        file.write(f"{i:X}")  # :X convierte en hexadecimal
                    file.write("\n")
                # Separar la matriz de las coordenadas.
                file.write("\n")
                # Guardar la entrada y la salida.
                file.write(f"{self.entry[0]},{self.entry[1]}\n")
                file.write(f"{self.exit[0]},{self.exit[1]}\n")
                # Guardar los movimientos de la solución.
                file.write(f"{self.solution}\n")
        except OSError as error:
            raise MazeConfigError(
                f"no se puede escribir el archivo de salida "
                f"'{self.op_file}': {error}"
            ) from error

    def maze_render(
            self,
            pos42: list[tuple[int, int]],
            solve: str,
            show_solution: bool = True
    ) -> None:
        """Dibuja el laberinto y su solución en la terminal."""

        # Convertir los movimientos de la solución(solve (ESNWSENW)) en coordenadas.
        # Celdas que forman el camino.
        draw_line: list[tuple[int, int]] = []
        draw_north: list[tuple[int, int]] = []  # Pasos verticales entre celdas.
        draw_west: list[tuple[int, int]] = []  # Pasos horizontales entre celdas.

        if show_solution:
            draw_line.append((self.entry[1], self.entry[0]))
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
                    row += 1   # Bajar una fila.
                    draw_line.append((row, column))
                    draw_north.append((row, column))  # Abertura norte de la celda actual.
                # Avanzar hacia el este.
                if i == "E":
                    column += 1  # Mover una columna a la derecha.
                    draw_line.append((row, column))
                    draw_west.append((row, column))  # Abertura oeste de la celda actual.
                # Avanzar hacia el oeste.
                if i == "W":
                    column -= 1  # Mover una columna a la izquierda.
                    draw_line.append((row, column))
                    draw_west.append((row, column + 1))  # Abertura oeste de la celda anterior.

        # Recorrer las filas del laberinto.
        # Dibujo del laberinto.
        for row in range(self.height):  # indica la fila que esta dibujando

            # Dibujamos las paredes NORTE
            for column in range(self.width):  # indica la columna
                if (row, column) in pos42:
                    print(f"{StyleColor.number_42}{"██"}{StyleColor.reset}", end="")
                else:
                    print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")  # 2 caracteres de unión

                # Dibujar la pared o el paso NORTE.
                if (row, column) in pos42:
                    print(f"{StyleColor.number_42}{"██" * 1}{StyleColor.reset}", end="")
                elif self.grid[row][column] & 1:
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
                for column in range(self.width):
                    # Dibujar la pared o el paso OESTE.
                    if (row, column) in pos42:
                        print(f"{StyleColor.number_42}{"██"}{StyleColor.reset}", end="")
                    elif self.grid[row][column] & 8:
                        print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")
                    # Pintar los pasos horizontales de la solución.
                    elif (row, column) in draw_west:
                        print(f"{StyleColor.solve}{"██"}{StyleColor.reset}", end="")
                    else:
                        print(f"{StyleColor.background}{"  "}{StyleColor.reset}", end="")

                    # Dibujar el interior de cada celda.
                    if (column, row) == self.exit:
                        print(f"{StyleColor.red}{"██" * 1}{StyleColor.reset}", end="")
                    elif (column, row) == self.entry:
                        print(f"{StyleColor.green}{"██" * 1}{StyleColor.reset}", end="")
                    elif (row, column) in pos42:
                        print(f"{StyleColor.number_42}{"██" * 1}{StyleColor.reset}", end="")
                    # dibujo de la linea
                    elif (row, column) in draw_line:
                        print(f"{StyleColor.solve}{"██"}{StyleColor.reset}", end="")
                    else:
                        print(f"{StyleColor.background}{"  " * 1}{StyleColor.reset}", end="")

                # Dibujamos Pared ESTE de la última celda del laberinto.
                if self.grid[row][self.width - 1] & 2:
                    print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")
                else:
                    print(f"{StyleColor.background}{"  "}{StyleColor.reset}", end="")
                print()  # terminamos paredes intermedias y centro

        # Dibujamos las paredes SUR del laberinto
        for column in range(self.width):
            if self.grid[self.height - 1][column] & 4:
                print(f"{StyleColor.wall}{"██" * 2}{StyleColor.reset}", end="")
            else:
                print(f"{StyleColor.background}{"  " * 2}{StyleColor.reset}", end="")
        print(f"{StyleColor.wall}{"██"}{StyleColor.reset}", end="")
        print()

    def maze_animation(self, pos42: list[tuple[int, int]]) -> None:
        """Anima progresivamente la solución del laberinto en la terminal."""
        for i in range(len(self.solution)):
            print("\033[H\033[J", end="")  # limppiar la terminal
            self.maze_render(pos42, self.solution[:i + 1], True)
            time.sleep(0.05)

    def maze_clean(self) -> None:
        self.solution = None
        self.grid = self.grid.clear()
