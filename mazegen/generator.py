from typing import Any

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
            grid: list[list[int]] = None
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
