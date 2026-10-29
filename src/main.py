#!/usr/bin/env python3

"""Read the maze configuration and draw its outer border."""
from style import StyleColor
from typing import Any
from maze import MazeCreate


def ReadConfig() -> dict[str, Any]:
    """Read the configuration file and return its values as a dictionary."""
    with open("config.txt") as config_file:
        config_dict: dict[str, Any] = {}
        for line in config_file:
            # Remove whitespace and ignore comments or empty lines.
            line = line.strip()

            if line.startswith("#") or line == "":
                continue
            # Split each configuration line into a key and a value.
            line_parts = line.split("=")

            if len(line_parts) == 2:
                key = line_parts[0]
                value = line_parts[1]

                # Convert maze dimensions to integers.
                if key == "WIDTH" or key == "HEIGHT":
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


def Drawlabyrinth(config: dict[str, Any]) -> None:
    """Draw the outer border using the configured width and height."""
    width = config["WIDTH"]
    height = config["HEIGHT"]

    # Draw the top border.
    for i in range(width):
        print(StyleColor.nostromo, end="")
    print()

    # Draw the side borders and the empty space between them.
    for i in range(height - 2):
        print(StyleColor.magratea, end="")

        for i in range((width *2) - 4):
            print(" ", end="")
        print(StyleColor.nautilus)

    # Draw the bottom border.
    for i in range(width):
        print(StyleColor.start, end="")
    print()


def ShowPosition(config: dict[str, Any]) -> None:
    entry = config["ENTRY"]
    exit_position = config["EXIT"]

    width = config["WIDTH"]
    height = config["HEIGHT"]

    print("Entry X:", entry[0])
    print("Entry Y:", entry[1])
    print("Exit X:", exit_position[0])
    print("Exit Y:", exit_position[1])

    if width <= 0:
        raise ValueError("Width must be greater than zero")

    if height <= 0:
        raise ValueError("Height must be greater than zero")

    if entry == exit_position:
        raise ValueError("Entry and exit cannot have the same coordinates")

    if entry[0] >= 0 and entry[0] < width:
        print("entry X is valid")
    else:
        raise ValueError("entry X is not valid")

    if entry[1] >= 0 and entry[1] < height:
        print("entry Y is valid")
    else:
        raise ValueError("entry Y is not valid")

    if exit_position[0] >= 0 and exit_position[0] < width:
        print("exit X is valid")
    else:
        raise ValueError("exit x is not valid")

    if exit_position[1] >= 0 and exit_position[1] < height:
        print("exit Y is valid")
    else:
        raise ValueError("exit Y is not valid")


# esto sería también el character chr(0x2588) o ██
if __name__ == "__main__":

    # Load the configuration and draw the labyrinth border.
    config = ReadConfig()
    Drawlabyrinth(config)
    ShowPosition(config)
    MazeCreate(config)