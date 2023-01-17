#!/usr/bin/python3

from termcolor import colored

TABLA = [
    [],
]

TABLA.append(
    [
        0,
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
        "pe",
        "pe",
        "pe",
        "pe",
    ]
)

TABLA.append(
    [
        0,
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
        "pe",
        "pe",
        "pe",
        "pe",
    ]
)

TABLA.append(
    [
        0,
        "pe",
        "pe",
        "pe",
        "di",
        "di",
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
        "di",
        "di",
        "di",
        "di",
        "di",
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
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
        "pe",
        "pe",
        "pe",
        "pe",
    ]
)

TABLA.append(
    [
        0,
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
    ]
)

TABLA.append(
    [
        0,
        "di",
        "di",
        "di",
        "di",
        "di",
        "pl",
        "di",
        "di",
        "pl",
        "pl",
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

TABLA.append(
    [
        0,
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
        "di",
    ]
)


def pares():
    mano = 0
    crupier = 0
    print("11 = A (mano)")

    while mano <= 0 or mano > 11 or crupier <= 0 or crupier > 10:
        mano = int(input("Tu mano es: Par de: "))
        crupier = int(input("La mano de ese we es: "))

    if mano == 21 or crupier == 21:
        print("Pq?")
        return

    print("\nTu mano es par de:", mano, "la mano del crupier es", crupier)
    des = TABLA[mano][crupier]

    if des == "pl":
        des = "Plantate"
    elif des == "pe":
        des = "Pide cartas"
    elif des == "do":
        des = "Dobla la apuesta"
    elif des == "di":
        des = "Divide tu mano"

    print("Lo que tienes que hacer es:", colored(des, "red"), "\n" * 2)
