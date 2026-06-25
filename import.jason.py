personajes = [
    {
        "nombre": "Goku",
        "raza": "Saiyajin",
        "nivel_poder": 9500,
        "planeta": "Tierra",
        "edad": 47,
        "alineacion": "Heroe",
        "transformaciones": [
            "Super Saiyajin",
            "Super Saiyajin 2",
            "Super Saiyajin 3",
            "Super Saiyajin Dios",
            "Ultra Instinto"
        ],
        "tecnicas": [
            "Kamehameha",
            "Genkidama",
            "Kaioken"
        ]
    },
    {
        "nombre": "Vegeta",
        "raza": "Saiyajin",
        "nivel_poder": 9300,
        "planeta": "Vegeta",
        "edad": 52,
        "alineacion": "Heroe",
        "transformaciones": [
            "Super Saiyajin",
            "Super Saiyajin 2",
            "Super Saiyajin Blue"
        ],
        "tecnicas": [
            "Final Flash",
            "Big Bang Attack",
            "Galick Gun"
        ]
    },
    {
        "nombre": "Gohan",
        "raza": "Hibrido",
        "nivel_poder": 8900,
        "planeta": "Tierra",
        "edad": 27,
        "alineacion": "Heroe",
        "transformaciones": [
            "Super Saiyajin",
            "Super Saiyajin 2",
            "Beast"
        ],
        "tecnicas": [
            "Masenko",
            "Kamehameha"
        ]
    },
    {
        "nombre": "Piccolo",
        "raza": "Namekiano",
        "nivel_poder": 8500,
        "planeta": "Namek",
        "edad": 32,
        "alineacion": "Heroe",
        "transformaciones": [
            "Orange Piccolo",
            "Poder Despertado"
        ],
        "tecnicas": [
            "Makankosappo",
            "Masenko"
        ]
    }
]

while True:

    print("\n===== MENU =====")
    print("1 - Mostrar personajes")
    print("2 - Buscar por raza")
    print("3 - Modificar personaje")
    print("4 - Eliminar personaje")
    print("5 - Ordenar personajes")
    print("6 - Personaje con más técnicas")
    print("7 - Personaje con menos transformaciones")
    print("8 - Salir")

    opcion = input("Ingrese opción: ")

    if opcion == "1":

        for p in personajes:
            print("\nNombre:", p["nombre"])
            print("Raza:", p["raza"])
            print("Edad:", p["edad"])

    elif opcion == "2":

        raza = input("Ingrese raza: ")

        for p in personajes:
            if p["raza"].lower() == raza.lower():

                print("\nNombre:", p["nombre"])
                print("Planeta:", p["planeta"])
                print("Poder:", p["nivel_poder"])

    elif opcion == "3":

        nombre = input("Personaje a modificar: ")

        encontrado = False

        for p in personajes:

            if p["nombre"].lower() == nombre.lower():

                encontrado = True

                print("1-Nombre")
                print("2-Raza")
                print("3-Edad")

                campo = input("Seleccione campo: ")

                if campo == "1":
                    p["nombre"] = input("Nuevo nombre: ")

                elif campo == "2":
                    p["raza"] = input("Nueva raza: ")

                elif campo == "3":
                    p["edad"] = int(input("Nueva edad: "))

                print("Modificación realizada.")

        if encontrado == False:
            print("No existe ese personaje.")

    elif opcion == "4":

        nombre = input("Nombre a eliminar: ")

        eliminado = False

        for p in personajes:

            if p["nombre"].lower() == nombre.lower():

                personajes.remove(p)
                eliminado = True
                print("Personaje eliminado.")
                break

        if eliminado == False:
            print("No encontrado.")

    elif opcion == "5":

        copia = personajes.copy()

        print("1-Nombre")
        print("2-Raza")
        print("3-Edad")

        criterio = input("Seleccione: ")

        if criterio == "1":
            copia.sort(key=lambda x: x["nombre"])

        elif criterio == "2":
            copia.sort(key=lambda x: x["raza"])

        elif criterio == "3":
            copia.sort(key=lambda x: x["edad"])

        for p in copia:
            print(p["nombre"], "-", p["raza"], "-", p["edad"])

    elif opcion == "6":

        mayor = personajes[0]

        for p in personajes:

            if len(p["tecnicas"]) > len(mayor["tecnicas"]):
                mayor = p

        print("\nPersonaje con más técnicas:")
        print(mayor["nombre"])
        print("Cantidad:", len(mayor["tecnicas"]))

    elif opcion == "7":

        menor = personajes[0]

        for p in personajes:

            if len(p["transformaciones"]) < len(menor["transformaciones"]):
                menor = p

        print("\nPersonaje con menos transformaciones:")
        print(menor["nombre"])
        print("Cantidad:", len(menor["transformaciones"]))

    elif opcion == "8":

        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")
