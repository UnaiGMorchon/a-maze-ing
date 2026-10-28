#!/usr/bin/env python3

from style import StyleColor

""" # verde
print(StyleColor.start)

# rojo
print(StyleColor.end)

# nautilus
print(StyleColor.nautilus)

# magratea
print(StyleColor.magratea)

# nostromo
print(StyleColor.nostromo)
 """



width = 20
height = 20
for i in range(width):
    print("██", end="")
print()

for i in range(height - 2):
    print("██", end="")
    for i in range((width *2) - 4):
        print(" ", end="")
    print("██")

for i in range(width):
    print("██", end="")
print()