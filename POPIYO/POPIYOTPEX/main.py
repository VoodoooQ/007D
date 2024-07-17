from funciones import asignar_sueldos_aleatorios, clasificar_sueldos, ver_estadisticas, reporte_sueldos, salir_programa

def menu():
    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            asignar_sueldos_aleatorios()
        elif opcion == 2:
            clasificar_sueldos()
        elif opcion == 3:
            ver_estadisticas()
        elif opcion == 4:
            reporte_sueldos()
        elif opcion == 5:
            salir_programa()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
