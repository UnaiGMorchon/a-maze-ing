#!/usr/bin/env python3

"""Validar los argumentos de línea de comandos y el archivo de config."""

from typing import Any
from . import pattern42

# Claves que el archivo de configuración debe incluir obligatoriamente.
REQUIRED_KEYS = ("WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT")


class MazeConfigError(Exception):
    """Error de configuración o de argumentos: se muestra sin traceback."""


def ValidateArgs(argv: list[str]) -> str:
    """Comprobar que se ha recibido exactamente un argumento (el config)."""
    program = argv[0] if argv else "a_maze_ing.py"

    if len(argv) != 2:
        raise MazeConfigError(
            f"uso: python3 {program} <config.txt> "
            f"(recibidos {len(argv) - 1} argumento(s), se esperaba 1)"
        )
    return argv[1]


def ParseConfigLines(lines: list[str]) -> dict[str, str]:
    """Convertir las líneas del archivo en un diccionario KEY -> VALUE.

    Acepta comentarios al final de línea (todo lo que vaya tras un '#'
    se ignora).
    """
    raw: dict[str, str] = {}

    for number, raw_line in enumerate(lines, start=1):
        line = raw_line.split("#", 1)[0].strip()

        if line == "":
            continue

        # Cada línea debe tener exactamente un signo '='.
        if line.count("=") != 1:
            raise MazeConfigError(
                f"línea {number} del config mal formada: {line!r} "
                "(se espera KEY=VALUE)"
            )

        key, value = (part.strip() for part in line.split("=", 1))
        if key == "" or value == "":
            raise MazeConfigError(
                f"línea {number} del config mal formada: "
                "clave o valor vacío"
            )
        raw[key.upper()] = value

    return raw


def ValidateConfig(raw: dict[str, str]) -> dict[str, Any]:
    """Validar los valores y convertirlos a los tipos usados por el resto."""
    missing = [key for key in REQUIRED_KEYS if key not in raw]
    if missing:
        raise MazeConfigError(
            f"faltan claves obligatorias en el config: {', '.join(missing)}"
        )

    config: dict[str, Any] = {}

    config["WIDTH"] = _ValidatePositiveInt(raw["WIDTH"], "WIDTH")
    config["HEIGHT"] = _ValidatePositiveInt(raw["HEIGHT"], "HEIGHT")

    if raw["PERFECT"] not in ("True", "False"):
        raise MazeConfigError(
            f"PERFECT debe ser 'True' o 'False' "
            f"(recibido {raw['PERFECT']!r})"
        )
    config["PERFECT"] = raw["PERFECT"] == "True"

    width, height = config["WIDTH"], config["HEIGHT"]
    if width * height < 2:
        raise MazeConfigError(
            "el laberinto es demasiado pequeño para tener "
            "ENTRY y EXIT distintos"
        )

    if width > 50:
        raise MazeConfigError(
            f"Ancho del laberinto supera el maximo de 25"
            f" (recibido {width})"
        )

    config["ENTRY"] = _ValidateCoordinate(raw["ENTRY"], "ENTRY", width, height)
    config["EXIT"] = _ValidateCoordinate(raw["EXIT"], "EXIT", width, height)

    if config["ENTRY"] == config["EXIT"]:
        raise MazeConfigError("ENTRY y EXIT no pueden ser la misma celda")

    positions_42 = pattern42.pattern42(config)
    entry = config["ENTRY"]
    exit = config["EXIT"]
    if (entry[1], entry[0]) in positions_42 or (exit[1], exit[0]) in positions_42:
        raise MazeConfigError("ENTRY o EXIT no pueden estar en la posiciones del 42")

    config["OP_FILE"] = raw["OUTPUT_FILE"]

    # SEED es opcional; si está presente debe ser un entero.
    if "SEED" in raw:
        try:
            config["SEED"] = int(raw["SEED"])
        except ValueError:
            raise MazeConfigError(
                f"SEED debe ser un número entero (recibido {raw['SEED']!r})"
            )

    # Conservar cualquier otra clave adicional no reconocida, tal cual.
    for key, value in raw.items():
        if key not in config:
            config[key] = value

    return config


def _ValidatePositiveInt(value: str, key: str) -> int:
    """Convertir value a int y comprobar que sea estrictamente positivo."""
    try:
        parsed = int(value)
    except ValueError:
        raise MazeConfigError(
            f"{key} debe ser un número entero (recibido {value!r})"
        )

    if parsed <= 0:
        raise MazeConfigError(f"{key} debe ser positivo (recibido {parsed})")
    return parsed


def _ValidateCoordinate(
    value: str, key: str, width: int, height: int
) -> tuple[int, int]:
    """Convertir 'x,y' a tupla de enteros y comprobar que esté en el mapa."""
    parts = value.split(",")
    if len(parts) != 2:
        raise MazeConfigError(
            f"{key} debe tener el formato x,y (recibido {value!r})"
        )

    try:
        x_coordinate, y_coordinate = int(parts[0]), int(parts[1])
    except ValueError:
        raise MazeConfigError(
            f"{key} debe contener enteros (recibido {value!r})"
        )

    if not (0 <= x_coordinate < width) or not (0 <= y_coordinate < height):
        raise MazeConfigError(
            f"{key}={x_coordinate},{y_coordinate} está fuera del "
            f"laberinto ({width}x{height})"
        )
    return (x_coordinate, y_coordinate)
