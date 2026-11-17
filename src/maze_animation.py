#!/usr/bin/env python3

import time
from typing import Any
from src.maze_render import MazeRender


def MazeAnimation(config: dict[str, Any], maze: list[list[int]], pos42: list[tuple[int, int]], solve: str) -> None:
    """Anima progresivamente la solución del laberinto en la terminal."""
    for i in range(len(solve)):
        print("\033[H\033[J", end="")  # limppiar la terminal
        MazeRender(config, maze, pos42, solve[:i + 1], True)
        time.sleep(0.05)