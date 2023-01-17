#!/usr/bin/python3

TABLA = [
    [],
]

TABLA.append(
    [
        0,
        "pe",
        "pe",
        "pe",
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
        "pe",
        "pe",
        "pe",
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
        "pe",
        "pe",
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
        "pe",
        "pe",
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
        "pl",
        "do",
        "do",
        "do",
        "do",
        "pl",
        "pl",
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


def suave():
    mano = 0
    crupier = 0

    while mano <= 0 or mano > 9 or crupier <= 0 or crupier > 10:
        mano = int(input("Tu mano es: A"))
        crupier = int(input("La mano de ese we es: "))

    if mano == 21 or crupier == 21:
        print("Pq?")
        return

    print("\nTu mano es", "A" + str(mano), "la mano del crupier es", crupier)
    des = TABLA[mano][crupier]

    if des == "pl":
        des = "Plantate"
    elif des == "pe":
        des = "Pide cartas"
    elif des == "do":
        des = "Dobla la apuesta"

    print("Lo que tienes que hacer es:", des, "\n" * 2)
