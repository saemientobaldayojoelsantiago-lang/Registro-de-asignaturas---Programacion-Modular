from estudiantes import estudiantes
from asignaturas import asignaturas


def asignar_asignatura():
    print("\n========================================")
    print("           ASIGNAR ASIGNATURA")
    print("========================================")

    print("\nSeleccione un estudiante:")

    for i, estudiante in enumerate(estudiantes, 1):
        print(f"{i}. {estudiante['nombre']}")

    estudiante = input("\nSeleccione una opción: ")

    print("\nSeleccione una asignatura:")

    for i, asignatura in enumerate(asignaturas, 1):
        print(f"{i}. {asignatura['nombre']}")

    asignatura = input("\nSeleccione una opción: ")

    print("\nMatrícula registrada.")

    input("\nPresione ENTER para continuar...")
