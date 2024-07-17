compradores = []
cantidada=[]
cantidadb=[]
cantidadc=[]
cantidadd=[]
def comprar(matriz):
    print(f"Escoja un departamento que desea comprar ")
    contador=11
    print(f"Piso\tTipo\n\t  A    B   C   D\n")
    for i in range (10):
        contador=contador-1
        print(contador,"\t" ,matriz[i,:])
    bucle=0
    try:
        while bucle ==0:
            tipo = str(input("Escoja que tipo de departamento desea, ingrese A,B,C,D  : "))
            while tipo != "A" and tipo !="a" and tipo != "B" and tipo !="b" and tipo != "C" and tipo !="c" and tipo != "D" and tipo !="d":
                tipo = str(input("Escoja que tipo de departamento desea, ingrese A,B,C,D  "))
            if tipo =="A" or tipo =="a":
                numtipo=0
            elif tipo =="B" or tipo =="b":
                 numtipo=1
            elif tipo =="C" or tipo =="c":
                 numtipo=2
            elif tipo =="D" or tipo =="d":
                 numtipo=3
            num = int(input("Ingrese el número de piso 1-10  "))
            while num<1 or num>10:
                num = int(input("Ingrese el número de piso 1-10  "))
            val= int(input(f"¿El departamento {tipo}{num} es correcto? Ingrese 1 para Si y 2 para NO  "))
            ## 10-(num)
            if matriz[10-num,numtipo]=='X': 
                print("El departamento no está disponible")
                
            else:
                
                bucle=1
        
        if val == 1:
            if tipo =="A" or tipo =="a":
                cfn= int(input("El precio total es de 3.800 UF, ¿Desea continuar? Ingrese 1 para SI y 2 para NO  "))
                while cfn <1 or cfn >2:
                    cfn= int(input("El precio total es de 3.800 UF, ¿Desea continuar? Ingrese 1 para SI y 2 para NO  ")) 
                if cfn ==1:
                    print("Está a un paso de comprar el departamento")
                    rut=str(input("Ingrese su RUT sin digito verificado ni puntos EJ 12345678  "))
                    while len(rut)!=8:
                        rut=str(input("Ingrese su RUT sin digito verificado ni puntos EJ 12345678  "))
                print("Operacion REALIZADA con Éxito")
                cantidada.append([1])
                matriz[10-num,0] = "X"
                compradores.append(rut)
                return(matriz)
            elif tipo =="B" or tipo =="b":
                cfn= int(input("El precio total es de 3.000 UF, ¿Desea continuar? Ingrese 1 para SI y 2 para NO  "))
                while cfn <1 or cfn >2:
                    cfn= int(input("El precio total es de 3.000 UF, ¿Desea continuar? Ingrese 1 para SI y 2 para NO  ")) 
                if cfn ==1:
                    print("Está a un paso de comprar el departamento  ")
                    rut=str(input("Ingrese su RUT sin digito verificado ni puntos EJ 12345678  "))
                    while len(rut)!=8:
                        rut=str(input("Ingrese su RUT sin digito verificado ni puntos EJ 12345678  "))
                print("Operacion REALIZADA con Éxito")
                cantidadb.append([1])
                matriz[10-num,1] = "X"
                compradores.append(rut)
                return(matriz)
            elif tipo =="C" or tipo =="c":
                cfn= int(input("El precio total es de 2.800 UF, ¿Desea continuar? Ingrese 1 para SI y 2 para NO  "))
                while cfn <1 or cfn >2:
                    cfn= int(input("El precio total es de 2.800 UF, ¿Desea continuar? Ingrese 1 para SI y 2 para NO  ")) 
                if cfn ==1:
                    print("Está a un paso de comprar el departamento")
                    rut=str(input("Ingrese su RUT sin digito verificado ni puntos EJ 12345678  "))
                    while len(rut)!=8:
                        rut=str(input("Ingrese su RUT sin digito verificado ni puntos EJ 12345678  "))
                print("Operacion REALIZADA con Éxito")
                cantidadc.append([1])
                matriz[10-num,2] = "X"
                compradores.append(rut)
                return(matriz)
            elif tipo =="D" or tipo =="d":
                cfn= int(input("El precio total es de 3.500 UF, ¿Desea continuar? Ingrese 1 para SI y 2 para NO  "))
                while cfn <1 or cfn >2:
                    cfn= int(input("El precio total es de 3.500 UF, ¿Desea continuar? Ingrese 1 para SI y 2 para NO  ")) 
                if cfn ==1:
                    print("Está a un paso de comprar el departamento  ")
                    rut=str(input("Ingrese su RUT sin digito verificado ni puntos EJ 12345678  "))
                    while len(rut)!=8:
                        rut=str(input("Ingrese su RUT sin digito verificado ni puntos EJ 12345678  "))
                print("Operacion REALIZADA con Éxito")
                cantidadd.append([1])
                matriz[10-num,3] = "X"
                compradores.append(rut)
                return(matriz)
                
    except ValueError:
        print("Error al ingresar el tipo de departamento")

def mostrar(restantes):
    contador=11
    print(f"Piso\tTipo\n\t  A    B   C   D\n")
    for i in range (10):
        contador=contador-1
        print(contador,"\t" ,restantes[i,:])

def lista():
    
    print(compradores)

def ganancias():
    print("Tipo de Departamento\tCantidad\tTotal")
    print(f"Tipo A 3800UF\t\t{len(cantidada)}\t{len(cantidada)*3800} UF")
    print(f"Tipo B 3000UF\t\t{len(cantidadb)}\t{len(cantidadb)*3000} UF")
    print(f"Tipo C 2800UF\t\t{len(cantidadc)}\t{len(cantidadc)*2800} UF")
    print(f"Tipo D 3500UF\t\t{len(cantidadd)}\t{len(cantidadd)*3500} UF")
    print(f"TOTAL \t\t\t {len(cantidada)+len(cantidadb)+len(cantidadc)+len(cantidadd)} \t {(len(cantidada)*3800)+(len(cantidadb)*3000)+(len(cantidadc)*2800)+(len(cantidadd)*3500)} UF")

def salir(flag):
    print("Saliendo del sistema, Adios!!!!!")
    print("Forma B 10/07/2023")
    flag=False
    return(flag)