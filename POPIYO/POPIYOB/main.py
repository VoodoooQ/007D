import numpy as np 
import func as fn 
flag=True
matriz = np.empty([10,4], dtype=str)
for i in range(10):
    for j in range (4):
        matriz[i,j] = j+1
##print(matriz)
while flag:
    print("Bienvenidos a ventas inmobiliaria CASA FELIZ")
    elec = int(input("Ingrese el número de la opción: \n\t1)Comprar departamento\n\t2)Mostrar departamentos disponibles\n\t3)Ver listado de compradores\n\t4)Mostrar ganancias totales\n\t5)Salir\n\t"))
    while elec <1 or elec>5 :
        elec = int(input("Error al ingresar dato,Ingrese el número de la opción: \n\t1)Ingresar\n\t2)Buscar\n\t3)Imprimir certificados\n\t4)Salir\n\t"))
    if elec == 1:
        matriz = fn.comprar(matriz)
    elif elec==2:
        fn.mostrar(matriz)
    elif elec==3:
        fn.lista()
    elif elec==4:
        fn.ganancias()
    elif elec==5:
        flag = fn.salir(flag)