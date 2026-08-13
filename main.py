from estudiantes import gestionar_estudiantes
from asignaturas import gestionar_asignaturas
from matriculas import asignar_asignatura
from consultas import consultar_registros


def menu_principal():
    while True:
        print("\n========================================")
        print("   SISTEMA DE REGISTRO DE ASIGNATURAS")
        print("========================================")
        print("1. Registrar / Modificar estudiantes")
        print("2. Registrar / Modificar asignaturas")
        print("3. Asignar asignatura")
        print("4. Consultar registros")
        print("5. Salir")
        print("========================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_estudiantes()

        elif opcion == "2":
            gestionar_asignaturas()

        elif opcion == "3":
            asignar_asignatura()

        elif opcion == "4":
            consultar_registros()

        elif opcion == "5":
            print("\nSaliendo del sistema...")
            break

        else:
            print("\nOpción no válida.")


menu_principal()
