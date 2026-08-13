asignaturas = [
    {
        "id": "001",
        "nombre": "Matemáticas"
    },
    {
        "id": "002",
        "nombre": "Inglés"
    }
]


def ingresar_datos():
    print("\n--- INGRESAR / MODIFICAR ASIGNATURA ---")

    print("ID: __________")
    print("Nombre de la asignatura: __________________")

    print("\nAsignatura agregada / modificada / eliminada.")


def guardar_datos():
    print("\nDatos guardados perfectamente.")


def gestionar_asignaturas():
    while True:
        print("\n========================================")
        print("      REGISTRAR / MODIFICAR ASIGNATURA")
        print("========================================")
        print("1. Ingresar datos")
        print("2. Guardar datos")
        print("3. Volver al menú")
        print("========================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_datos()

        elif opcion == "2":
            guardar_datos()

        elif opcion == "3":
            break

        else:
            print("\nOpción no válida.")
