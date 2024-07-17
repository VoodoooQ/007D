import random
import csv
import numpy as np

trabajadores = ["Juan Pérez", "María Garcia", "Carlos López", "Ana Martinez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
cargos = ["Consultor TI", "Analista", "Programador", "Jefe de Proyecto"]

def asignar_sueldos():
    sueldos = {}
    for trabajador in trabajadores:
        sueldos[trabajador] = random.randint(300000, 2500000)
    return sueldos

def clasificar_sueldos(sueldos):
    menores_800k = []
    entre_800k_y_2m = []
    superiores_2m = []
    for trabajador in sueldos:
        sueldo = sueldos[trabajador]
        cargo = random.choice(cargos)
        if sueldo < 800000:
            menores_800k.append((trabajador, cargo, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800k_y_2m.append((trabajador, cargo, sueldo))
        else:
            superiores_2m.append((trabajador, cargo, sueldo))
    return menores_800k, entre_800k_y_2m, superiores_2m

def ver_estadisticas(sueldos):
    sueldos_lista = []
    for sueldo in sueldos.values():
        sueldos_lista.append(sueldo)
    sueldo_max = max(sueldos_lista)
    sueldo_min = min(sueldos_lista)
    sueldo_promedio = sum(sueldos_lista) / len(sueldos_lista)
    sueldo_geom = np.exp(np.mean(np.log(sueldos_lista)))
    return sueldo_max, sueldo_min, sueldo_promedio, sueldo_geom

def generar_reporte(sueldos):
    reporte = []
    for trabajador in sueldos:
        sueldo = sueldos[trabajador]
        cargo = random.choice(cargos)
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        reporte.append([trabajador, cargo, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre Empleado", "Cargo", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        writer.writerows(reporte)

def mostrar_menu():
    sueldos = {}
    while True:
        print("\nMenú de Opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            sueldos = asignar_sueldos()
            print("Sueldos asignados aleatoriamente.")
        elif opcion == '2':
            if not sueldos:
                print("Primero debe asignar los sueldos.")
            else:
                menores_800k, entre_800k_y_2m, superiores_2m = clasificar_sueldos(sueldos)
                print("\nSueldos menores a 800.000 TOTAL:", len(menores_800k))
                for emp in menores_800k:
                    print(emp[0], emp[1], f"${emp[2]:,.0f}")
                print("\nSueldos entre 800.000 y 2.000.000 TOTAL:", len(entre_800k_y_2m))
                for emp in entre_800k_y_2m:
                    print(emp[0], emp[1], f"${emp[2]:,.0f}")
                print("\nSueldos superiores a 2.000.000 TOTAL:", len(superiores_2m))
                for emp in superiores_2m:
                    print(emp[0], emp[1], f"${emp[2]:,.0f}")
                total_sueldos = sum(sueldos.values())
                print(f"\nTOTAL SUELDOS: ${total_sueldos:,.0f}")
        elif opcion == '3':
            if not sueldos:
                print("Primero debe asignar los sueldos.")
            else:
                sueldo_max, sueldo_min, sueldo_promedio, sueldo_geom = ver_estadisticas(sueldos)
                print(f"\nSueldo más alto: ${sueldo_max:,.0f}")
                print(f"Sueldo más bajo: ${sueldo_min:,.0f}")
                print(f"Promedio de sueldos: ${sueldo_promedio:,.0f}")
                print(f"Media geométrica de sueldos: ${sueldo_geom:,.0f}")
        elif opcion == '4':
            if not sueldos:
                print("Primero debe asignar los sueldos.")
            else:
                generar_reporte(sueldos)
                print("Reporte de sueldos generado en 'reporte_sueldos.csv'.")
        elif opcion == '5':
            print("\nFinalizando programa.....")
            print("Desarrollado por [Maximiliano Diaz]")
            print("RUT[20.389.269-1]")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
