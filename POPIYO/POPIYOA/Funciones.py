import numpy as np

lugaresComprados = []
lugaresConcierto = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
])

recaudacionConcierto = {
    "PLATINUM": [0, 0],
    "GOLD": [0, 0],
    "SILVER": [0, 0],
}

def updateRecaudacionConcierto(tipoEntrada, costoEntrada):
    recaudacionConcierto[tipoEntrada][0] = recaudacionConcierto[tipoEntrada][0] + 1
    recaudacionConcierto[tipoEntrada][1] = recaudacionConcierto[tipoEntrada][1] + costoEntrada

def comprarEntradas():
    print("~~~ COMPRA DE ENTRADAS ~~~\n")
    print("~~ PLATINUM: $120,000 (Asiento del 1 al 20)")
    print("~~ GOLD: $80,000 (Asiento del 21 al 50)")
    print("~~ SILVER: $50,000 (Asiento del 51 al 100)\n")

    opEntradas = int(input("Ingresa la cantidad de entradas que deseas adquirir (Minimo 1 y Maximo 3): "))
    if opEntradas >= 1 and opEntradas <= 3:
        contadorEntradas = 0
        while contadorEntradas < opEntradas:
            mostrarLugares()

            print(f"\n~~ ENTRADA N° {contadorEntradas + 1}")
            print("[⛔] ¡Las filas se cuentan de arriba hacia abajo!\n")
            opFila = int(input("Ingresa la fila del asiento que vas a adquirir (Entre 0 y 9): "))
            if opFila >= 0 and opFila <= 9:
                mostrarFila(opFila)
                
                print("[⛔] ¡Los asientos se cuentan de izquerda a derecha!\n")
                opAsiento = int(input("Ingresa el asiento que vas a adquirir (Entre 0 y 9): "))
                if opAsiento >= 0 and opAsiento <= 9:
                    if not lugaresConcierto[opFila][opAsiento] == "X":
                        numeroAs = int(lugaresConcierto[opFila][opAsiento])

                        print("[⛔] ¡El rut no debe contener puntos, guiones ni digito verificador!\n")
                        opIdentificador = str(input("Ingresa el rut del propietario de este asiento: "))

                        opNombre = str(input("Ingresa el nombre del propietario del asiento: "))
                        
                        if numeroAs >= 1 and numeroAs <= 20:
                            tipoEntrada = "PLATINUM"
                            updateRecaudacionConcierto(tipoEntrada, 120000)
                        elif numeroAs >= 21 and numeroAs <= 50:
                            tipoEntrada = "GOLD"
                            updateRecaudacionConcierto(tipoEntrada, 80000)
                        elif numeroAs >= 51 and numeroAs <= 100:
                            tipoEntrada = "SILVER"
                            updateRecaudacionConcierto(tipoEntrada, 50000)

                        contadorEntradas = contadorEntradas + 1
                        lugaresComprados.append([opNombre, opIdentificador, numeroAs, tipoEntrada])
                        lugaresConcierto[opFila][opAsiento] = "X"
 
                        print("\n~~ [CREATIVOS.CL] ¡Compra realizada correctamente!")
                        print(f"~~ [CREATIVOS.CL] Asiento N°{numeroAs} registrado a nombre de {opNombre} con el rut {opIdentificador}\n")
                    else:
                        print("[⛔] ¡Este asiento ya se encuentra ocupado!")
                else:
                    print("[⛔] ¡Numero de asiento incorrecto!")
            else:
                print("[⛔] ¡Numero de fila incorrecto!")
    else:
        print("[⛔] ¡Solo se permite adquirir entre 1 y 3 entradas por persona!")

def mostrarLugares():
    print("\n~~~ Lugares Disponibles ~~~")
    print(lugaresConcierto)

def mostrarFila(numeroFila):
    print(lugaresConcierto[numeroFila])

def mostrarAsistentes():
    print("\n~~~ LISTADO DE ASISTENTES ~~~")
    for x in lugaresComprados:
        print(f"Comprador: {x[0]}")
        print(f"RUT: {x[1]}")
        print(f"Numero de Asiento: {x[2]}")
        print(f"Tipo Entrada: {x[3]}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def mostrarGanancias():
    print("\n~~~ GANANCIAS ENTRADAS PLATINUM ~~~")
    print(f"Total de entradas premium vendidas: {recaudacionConcierto['PLATINUM'][0]}")
    print(f"Total de dinero recaudado: ${recaudacionConcierto['PLATINUM'][1]:,}")
    print("~~~ GANANCIAS ENTRADAS GOLD ~~~")
    print(f"Total de entradas gold vendidas: {recaudacionConcierto['GOLD'][0]}")
    print(f"Total de dinero recaudado: ${recaudacionConcierto['GOLD'][1]:,}")
    print("~~~ GANANCIAS ENTRADAS SILVER ~~~")
    print(f"Total de entradas silver vendidas: {recaudacionConcierto['SILVER'][0]}")
    print(f"Total de dinero recaudado: ${recaudacionConcierto['SILVER'][1]:,}\n")
    print("~~~ ESTADISTICAS GENERALES ~~~")
    print(f"Total de entradas del concierto vendidas: {recaudacionConcierto['PLATINUM'][0] + recaudacionConcierto['GOLD'][0] + recaudacionConcierto['SILVER'][0]}")
    print(f"Total de dinero recaudado con el concierto: ${recaudacionConcierto['PLATINUM'][1] + recaudacionConcierto['GOLD'][1] + recaudacionConcierto['SILVER'][1]:,}\n")