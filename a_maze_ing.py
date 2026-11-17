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


def ReadConfig(filename: str) -> dict[str, Any]:
    """Read the configuration file and return its values as a dictionary."""
    with open(filename) as config_file:
        config_dict: dict[str, Any] = {}
        for line in config_file:
            # Remove whitespace and ignore comments or empty lines.
            line = line.split("#")[0].strip()

            if line == "":
                continue
            # Split each configuration line into a key and a value.
            line_parts = line.split("=")

            if len(line_parts) == 2:
                key = line_parts[0].strip()  # quitamos espacios
                value = line_parts[1].strip()  # quitamos espacios

                # Convert maze dimensions to integers.
                if key == "WIDTH" or key == "HEIGHT" or key == "SEED":
                    value = int(value)

                # Convert the PERFECT setting to a boolean.
                if key == "PERFECT":
                    value = value == "True"

                # Convert entry and exit coordinates to integer tuples.
                if key == "ENTRY" or key == "EXIT":
                    coordinates = value.split(",")
                    x_coordinate = int(coordinates[0])
                    y_coordinate = int(coordinates[1])
                    coodenates_position: tuple[int, int] = (x_coordinate, y_coordinate)
                    value = coodenates_position
                # Store the converted value in the configuration dictionary.
                config_dict[key] = value
        return(config_dict)


# esto sería también el character chr(0x2588) o ██
if __name__ == "__main__":
    # Load the configuration and draw the labyrinth border.
    config = ReadConfig(sys.argv[1])
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
    maze = MazeCreate(config)
    print("SEED:", seed)
    print("TIPO:", type(seed))

    # Genera los caminos y devuelve las posiciones del 42, que guardas en pos. y semilla
    pos42 = GeneratorMaze(config, maze, seed, False)

    # Buscar el camino más corto entre entrada y salida.
    solve = MazeSolve(config, maze)
    # Guardar el laberinto y su solución en un archivo
    MazeSave(config, maze, solve)
    # Mostrar el laberinto y la solución en la terminal.
    MazeRender(config, maze, pos42, solve, True) # recibe el laberinto y las posiciones del 42 para poder dibujarlo ademas de la solución.

    show_solution= True
    color_index = 1

    while True:
        print("1. Re-generate a new maze")
        print("2. Show / Hide the shortest path")
        print("3. Rotate the wall colours")
        print("4. Animation maze")
        print("5. Animation solve")
        print("6. Quit")
        choice = input("choice? (1-6): ")
        if choice == "1":
            maze = MazeCreate(config)
            pos42 = GeneratorMaze(config, maze, seed, False)
            solve = MazeSolve(config, maze)
            MazeSave(config, maze, solve)
            MazeRender(config, maze, pos42, solve, show_solution)
        elif choice == "2":
            show_solution = not show_solution
            MazeRender(config, maze, pos42, solve, show_solution)
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
            MazeRender(config, maze, pos42, solve, show_solution)
        elif choice == "4":
            maze = MazeCreate(config)
            pos42 = GeneratorMaze(config, maze, seed, True)
            solve = MazeSolve(config, maze)
            MazeSave(config, maze, solve)
            MazeRender(config, maze, pos42, solve, show_solution)
        elif choice == "5":
            MazeAnimation(config, maze, pos42, solve)
        elif choice == "6":
            break
            
