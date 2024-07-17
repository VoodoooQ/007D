import Funciones as fn
Flag = True

while Flag:
    try:
        print("\n~~~ CREATIVOS.CL ~~~")
        print("[1] Comprar entradas")
        print("[2] Mostrar ubicaciones disponibles")
        print("[3] Ver listado de asistentes")
        print("[4] Mostrar ganancias totales")
        print("[5] Salir")

        op = int(input("\nIngresa una opcion de la lista (Entre 1 y 5): "))
        if op == 1:
            fn.comprarEntradas()
        elif op == 2:
            fn.mostrarLugares()
        elif op == 3:
            fn.mostrarAsistentes()
        elif op == 4:
            fn.mostrarGanancias()
        elif op == 5:
            Flag = False
            print("\n¡Adios!\nForma A - 10/07/2023\n")
        else:
            print("¡La opcion ingresada esta fuera de rango!")
    except (ValueError):
        Flag = False
        print("¡El valor ingresado no es valido!")
    except (KeyboardInterrupt):
        Flag = False
        print("\n¡Programa detenido a la fuerza por el usuario!")