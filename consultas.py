from estudiantes import estudiantes


def consultar_registros():
    print("\n========================================")
    print("          CONSULTAR REGISTROS")
    print("========================================")

    for estudiante in estudiantes:
        print(f"\nID: {estudiante['id']}")
        print(f"Nombre: {estudiante['nombre']}")
        print("Asignaturas:")

        for asignatura in estudiante["asignaturas"]:
            print(f"- {asignatura}")

    input("\nPresione ENTER para continuar...")
