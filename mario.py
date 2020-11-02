from cs50 import get_int

# Getting user input
while (True):
    height = get_int("Height: ")
    if (height in range(1, 9)):
        break

# Printing piramide
space_counter = height - 1
for i in range(height):
    print(" " * (space_counter - i) + "#" * (i + 1) + "  " + "#" * (i + 1))