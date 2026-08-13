estudiantes = [
    {
        "id": "001",
        "nombre": "Ana López",
        "asignaturas": ["Matemáticas"]
    },
    {
        "id": "002",
        "nombre": "Juan Pérez",
        "asignaturas": ["Inglés"]
    }
]


def ingresar_datos():
    print("\n--- INGRESAR / MODIFICAR ESTUDIANTE ---")

    print("ID: __________")
    print("Nombre: __________________")
    print("Asignaturas: __________________")

    print("\nEstudiante agregado / modificado / eliminado.")


def guardar_datos():
    print("\nDatos guardados perfectamente.")


def gestionar_estudiantes():
    while True:
        print("\n========================================")
        print("      REGISTRAR / MODIFICAR ESTUDIANTE")
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
