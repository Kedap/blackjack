#!/usr/bin/python3

import dura
import suave
import pares

print("--==[ Jack nigga ]==--", "\n")
print("q: Salir", "\n")


# Prompt
while True:
    print("1) Numero. 2) Con ass. 3) Pares.")
    opcion = input("> ")

    # Retorno facil
    if opcion == "q":
        exit(0)
    elif int(opcion) > 3 or int(opcion) <= 0:
        print("La opcion", opcion, "es incorrecta. Intenta de new")
        continue

    print("\n" * 2)

    if opcion == "1":
        dura.dura()
    elif opcion == "2":
        suave.suave()
    elif opcion == "3":
        pares.pares()
