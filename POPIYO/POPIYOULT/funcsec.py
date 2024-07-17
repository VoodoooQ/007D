import random
import csv
import numpy as np

trabajadores = ["Juan Pérez", "María Garcia", "Carlos López", "Ana Martinez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
cargos = ["Consultor TI", "Analista", "Programador", "Jefe de Proyecto"]

def asignar_sueldos():
    sueldos = {}
    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000)
        sueldos[trabajador] = sueldo
    return sueldos

def clasificar_sueldos(sueldos):
    menores_800k = []
    entre_800k_y_2m = []
    superiores_2m = []
    for trabajador in sueldos.keys():
        sueldo = sueldos[trabajador]
        cargo = random.choice(cargos)
        if sueldo < 800000:
            menores_800k.append((trabajador, cargo, sueldo))
        elif sueldo >= 800000 and sueldo <= 2000000:
            entre_800k_y_2m.append((trabajador, cargo, sueldo))
        else:
            superiores_2m.append((trabajador, cargo, sueldo))
    return menores_800k, entre_800k_y_2m, superiores_2m

def ver_estadisticas(sueldos):
    sueldos_lista = list(sueldos.values())
    sueldo_max = max(sueldos_lista)
    sueldo_min = min(sueldos_lista)
    sueldo_promedio = sum(sueldos_lista) / len(sueldos_lista)
    sueldo_geom = np.exp(np.mean(np.log(sueldos_lista)))
    return sueldo_max, sueldo_min, sueldo_promedio, sueldo_geom

def generar_reporte(sueldos):
    reporte = []
    for trabajador in sueldos.keys():
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
