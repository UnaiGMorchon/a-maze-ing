#!/usr/bin/env python3

class StyleColor():
        start: str = "\033[32m██\033[0m"
        end: str = "\033[31m██\033[0m"
        nautilus: str = "\033[38;2;0;186;188m██\033[0m"
        magratea: str = "\033[38;2;227;170;64m██\033[0m"
        nostromo: str = "\033[38;2;158;40;226m██\033[0m"








# esto sería también el character chr(0x2588) o ██
if __name__ == "__main__":
    #print(chr(0x2588) + chr(0x2588))
    #print("██")
    # verde
    print(StyleColor.start)

    # rojo 
    print(StyleColor.end)

    # teal nautilus
    print(StyleColor.nautilus)

    # Naranja magratea
    print(StyleColor.magratea)

    # morado nostromo
    print(StyleColor.nostromo)


""" 
    # verde
    print("\033[32m██\033[0m")
    # rojo 
    print("\033[31m██\033[0m")
    # teal nautilus
    print("\033[38;2;0;186;188m██\033[0m")
    # Naranja magratea
    print("\033[38;2;227;170;64m██\033[0m")
    # morado nostromo
    print("\033[38;2;158;40;226m██\033[0m") """