#!/usr/bin/env python3

"""Define the colors used to display the labyrinth in the terminal."""

""" USO
# verde
print(StyleColor.start)
# rojo
print(StyleColor.end)
# nautilus
print(StyleColor.nautilus)
# magratea
print(StyleColor.magratea)
# nostromo
print(StyleColor.nostromo)
    #print(chr(0x2588) + chr(0x2588))
    #print("██")

 """

class StyleColor():
        """ANSI color codes for drawing colored blocks."""
        # Green block
        start: str = "\033[32m██\033[0m"
        # Red block.
        end: str = "\033[31m██\033[0m"
        # Purple block.
        nautilus: str = "\033[38;2;0;186;188m██\033[0m"
        # Orange block.
        magratea: str = "\033[38;2;227;170;64m██\033[0m"
        # Turquoise block.
        nostromo: str = "\033[38;2;158;40;226m██\033[0m"



