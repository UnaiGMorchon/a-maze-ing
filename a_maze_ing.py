#!/usr/bin/env python3

"""Read the maze configuration and draw its outer border."""
import sys
from src.style import StyleColor
from typing import Any
from src.maze_create import MazeCreate
from src.maze_generator import GeneratorMaze
from src.maze_render import MazeRender
from src.maze_export import MazeSave
from src.maze_solve import MazeSolve
from src.maze_animation import MazeAnimation

from src.maze_validate import (
    MazeConfigError,
    ParseConfigLines,
    ValidateArgs,
    ValidateConfig,
)


def ReadConfig(path: str) -> dict[str, Any]:
    """Leer el archivo de configuración y devolver sus valores ya validados."""
    try:
        with open(path, encoding="utf-8") as config_file:
            lines = config_file.readlines()
    except OSError as error:
        raise MazeConfigError(
            f"no se puede leer el archivo de configuración '{path}': {error}"
        ) from error

    raw = ParseConfigLines(lines)
    return ValidateConfig(raw)


def Run(argv: list[str]) -> int:
    """Ejecutar el programa completo y devolver el código de salida."""
    try:
        config_path = ValidateArgs(argv)
        config = ReadConfig(config_path)

        # Crear la matriz con todas las paredes cerradas.
        maze = MazeCreate(config)
        # Genera los caminos y devuelve las posiciones del 42.
        pos42 = GeneratorMaze(config, maze)
        # Buscar el camino más corto entre entrada y salida.
        solve = MazeSolve(config, maze)
        # Guardar el laberinto y su solución en un archivo.
        MazeSave(config, maze, solve)
        # Mostrar el laberinto y la solución en la terminal.
        MazeRender(config, maze, pos42, solve)
    except (MazeConfigError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    except Exception as error:  # red de seguridad: nunca cerrar sin avisar
        print(f"Error inesperado: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(Run(sys.argv))
