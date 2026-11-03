#!/usr/bin/env pyton3

from typing import Any

def MazeSave(config: dict[str, Any], maze: list[list[int]]) -> None:
    output_file = config["OUTPUT_FILE"]
    entry = config["ENTRY"]
    exit = config["EXIT"]
    
    with open(output_file, "w", encoding="utf-8") as file:
        for row in maze:
            for i in row:
                file.write(f"{i:X}")  # :X convierte en hexadecimal
            file.write("\n")
        file.write("\n")
        file.write(f"{entry[0]},{entry[1]}\n")
        file.write(f"{exit[0]},{exit[1]}\n")



