#!/usr/bin/python3

from termcolor import colored

TABLA = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

TABLA.append(
    [
        0,
        "pe",
        "do",
        "do",
        "do",
        "do",
        "pe",
        "pe",
        "pe",
        "pe",
        "pe",
    ]
)

TABLA.append(
    [
        0,
        "do",
        "do",
        "do",
        "do",
        "do",
        "do",
        "do",
        "do",
        "pe",
        "pe",
    ]
)

TABLA.append(
    [
        0,
        "do",
        "do",
        "do",
        "do",
        "do",
        "do",
        "do",
        "do",
        "do",
        "pe",
    ]
)

TABLA.append(
    [
        0,
        "pe",
        "pe",
        "pe",
        "pl",
        "pl",
        "pe",
        "pe",
        "pe",
        "pe",
        "pe",
    ]
)

TABLA.append(
    [
        0,
        "pl",
        "pl",
        "pl",
        "pl",
        "pl",
        "pe",
        "pe",
        "pe",
        "pe",
        "pe",
    ]
)

TABLA.append(
    [
        0,
        "pl",
        "pl",
        "pl",
        "pl",
        "pl",
        "pe",
        "pe",
        "pe",
        "pe",
        "pe",
    ]
)

TABLA.append(
    [
        0,
        "pl",
        "pl",
        "pl",
        "pl",
        "pl",
        "pe",
        "pe",
        "pe",
        "pe",
        "pe",
    ]
)

TABLA.append(
    [
        0,
        "pl",
        "pl",
        "pl",
        "pl",
        "pl",
        "pe",
        "pe",
        "pe",
        "pe",
        "pe",
    ]
)

TABLA.append(
    [
        0,
        "pl",
        "pl",
        "pl",
        "pl",
        "pl",
        "pl",
        "pl",
        "pl",
        "pl",
        "pl",
    ]
)


def dura():
    mano = 0
    crupier = 0

    while mano <= 0 or mano > 21 or crupier <= 0 or crupier > 10:
        mano = int(input("Tu mano es: "))
        crupier = int(input("La mano de ese we es: "))

    if mano == 21 or crupier == 21:
        print("Pq?")
        return
    elif mano <= 8:
        print("Pide")
        return
    elif mano >= 17:
        print("Plantate ue")
        return

    print("\nTu mano es", mano, "la mano del crupier es", crupier)
    des = TABLA[mano][crupier]

    if des == "pl":
        des = "Plantate"
    elif des == "pe":
        des = "Pide cartas"
    elif des == "do":
        des = "Dobla la apuesta"

    print("Lo que tienes que hacer es:", colored(des, "red"), "\n" * 2)
