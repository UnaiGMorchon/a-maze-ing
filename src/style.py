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
    """ANSI color codes for the maze."""

    # Colores de texto (38)
    nautilus: str = "\033[38;2;0;186;188m"
    magratea: str = "\033[38;2;227;170;64m"
    nostromo: str = "\033[38;2;158;40;226m"
    green: str = "\033[32m"
    red: str = "\033[31m"
    black: str = "\033[30m"
    white: str = "\033[37m"

    # Colores de fondo (48)
    nautilus_back: str = "\033[48;2;0;186;188m"
    magratea_back: str = "\033[48;2;227;170;64m"
    nostromo_back: str = "\033[48;2;158;40;226m"

    """ # Colores de fondo aclarados un 50 % hacia blanco
    nautilus_back_half: str = "\033[48;2;128;221;222m"
    magratea_back_half: str = "\033[48;2;241;213;159m"
    nostromo_back_half: str = "\033[48;2;207;148;241m" """

    # Colores de fondo aclarados un 70 % hacia blanco
    nautilus_back_half: str = "\033[48;2;179;234;235m"
    magratea_back_half: str = "\033[48;2;247;230;198m"
    nostromo_back_half: str = "\033[48;2;226;191;246m"


    # Colores oscuros para destacar el 42
    nautilus_dark: str = "\033[38;2;0;102;106m"
    nostromo_dark: str = "\033[38;2;101;18;155m"
    magratea_dark: str = "\033[38;2;152;96;0m"


    green_back: str = "\033[42m"
    red_back: str = "\033[41m"
    black_back: str = "\033[40m"
    white_back: str = "\033[47m"

    # Restablecer colores
    reset: str = "\033[0m"

    # Colores de los elementos del laberinto
    wall: str = nautilus
    background: str = nautilus_back_half
    number_42: str = nautilus_dark
    start: str = green
    end: str = red
