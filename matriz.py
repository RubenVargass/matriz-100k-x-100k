import os
import random

FILAS = 100000
COLUMNAS = 100000
BLOQUE = 1000  # escribir 1000 bytes a la vez

with open("matriz.bin", "wb") as archivo:
    for _ in range(FILAS):
        for _ in range(0, COLUMNAS, BLOQUE):
            bloque = bytearray(random.getrandbits(1) for _ in range(BLOQUE))
            archivo.write(bloque)

print("Matriz creada por bloques directamente en disco.")