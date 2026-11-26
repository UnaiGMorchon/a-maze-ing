#!/usr/bin/env python3

"""Read the maze configuration and draw its outer border."""
import sys
from src.style import StyleColor
from typing import Any
from src.style import StyleColor
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
from mazegen import MazeGenerator


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


if __name__ == "__main__":
    """Ejecutar el programa completo y devolver el código de salida."""
    try:
        # Load the configuration and draw the labyrinth border.
        config_path = ValidateArgs(sys.argv)
        config = ReadConfig(config_path)
        seed = config.get("SEED")
        #print(config["PERFECT"])
        #print(type(config["PERFECT"]))

        #print(type(config["WIDTH"]))
        #print(type(config["HEIGHT"]))
        #print(type(config["ENTRY"]))
        #print(type(config["PERFECT"]))

        #Drawlabyrinth(config)
        #ShowPosition(config)

        # Crear la matriz con todas las paredes cerradas.
        maze = MazeGenerator(
            config["WIDTH"],
            config["HEIGHT"],
            config["ENTRY"],
            config["EXIT"],
            config["OP_FILE"],
            config["PERFECT"]
        )
        maze.maze_create()
        #print("SEED:", seed)
        #print("TIPO:", type(seed))

        # Genera los caminos y devuelve las posiciones del 42, que guardas en pos. y semilla
        pos42 = maze.maze_paths()

        # Buscar el camino más corto entre entrada y salida.
        solve = maze.maze_solve()
        # Guardar el laberinto y su solución en un archivo
        maze.maze_save()
        # Mostrar el laberinto y la solución en la terminal.
        maze.maze_render(pos42, True) # recibe el laberinto y las posiciones del 42 para poder dibujarlo ademas de la solución.
    except (MazeConfigError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
    except Exception as error:  # red de seguridad: nunca cerrar sin avisar
        print(f"Error inesperado: {error}", file=sys.stderr)
        sys.exit(1)

    show_solution= True
    color_index = 1

    while True:
        try:
            print("1. Re-generate a new maze")
            print("2. Show / Hide the shortest path")
            print("3. Rotate the wall colours")
            print("4. Animation maze")
            print("5. Animation solve")
            print("6. Quit")
            choice = input("choice? (1-6): ")
            if choice == "1":
                maze.maze_clean()
                maze.maze_create()
                pos42 = maze.maze_paths()
                solve = maze.maze_solve()
                maze.maze_save()
                maze.maze_render(pos42,  show_solution)
            elif choice == "2":
                show_solution = not show_solution
                maze.maze_render(pos42, show_solution)
            elif choice == "3":
                if color_index == 0:
                    StyleColor.wall = StyleColor.nautilus
                    StyleColor.background = StyleColor.nautilus_back_half
                    StyleColor.number_42 = StyleColor.nautilus_dark
                    color_index += 1
                elif color_index == 1:
                    StyleColor.wall = StyleColor.magratea
                    StyleColor.background = StyleColor.magratea_back_half
                    StyleColor.number_42 = StyleColor.magratea_dark
                    color_index += 1
                elif color_index == 2:
                    StyleColor.wall = StyleColor.nostromo
                    StyleColor.background = StyleColor.nostromo_back_half
                    StyleColor.number_42 = StyleColor.nostromo_dark
                    color_index = 0
                maze.maze_render(pos42, show_solution)
            elif choice == "4":
                maze.maze_clean()
                maze.maze_create()
                pos42 = maze.maze_paths(True)
                solve = maze.maze_solve()
                maze.maze_save()
                maze.maze_render(pos42, show_solution)
            elif choice == "5":
                maze.maze_animation(pos42)
            elif choice == "6":
                break
        except KeyboardInterrupt:
            print(f"\nKeyboard interrupt", file=sys.stderr)
            sys.exit(1)
        except Exception as error:
            print(f"Error inesperado: {error}", file=sys.stderr)
            sys.exit(1)
