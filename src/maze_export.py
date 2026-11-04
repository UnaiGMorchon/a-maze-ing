#!/usr/bin/env pyton3

from typing import Any

def MazeSave(config: dict[str, Any], maze: list[list[int]], solve: str) -> None:
    """Guarda el laberinto y su solución en un archivo."""
    output_file = config["OUTPUT_FILE"]
    entry = config["ENTRY"]
    exit = config["EXIT"]

    # Abrir el archivo en modo escritura.
    with open(output_file, "w", encoding="utf-8") as file:
        # Guardar cada fila del laberinto en hexadecimal.
        for row in maze:
            for i in row:
                file.write(f"{i:X}")  # :X convierte en hexadecimal
            file.write("\n")
        # Separar la matriz de las coordenadas.
        file.write("\n")
        # Guardar la entrada y la salida.
        file.write(f"{entry[0]},{entry[1]}\n")
        file.write(f"{exit[0]},{exit[1]}\n")
        # Guardar los movimientos de la solución.
        file.write(f"{solve}\n")




