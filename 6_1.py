
juego_ganado = False
cordenadas_circulo=[]
cont=0
no_cobreescribir=[]



def generaMatriz(num_f, num_c, valor):
    return [[valor for c in range(0, num_c)] for f in range(0, num_f)]

matriz = generaMatriz(3, 3 , "''")






def validar_sobreescrbir(valor, cual, array ):
    if len(array) <=1 or len(array) >= 3 or array[1]=="" or array[0]=="":
        print("Ingrese 2 valores")
        return False
    if array[1]=="1" or array[1]=="2" or array[1]=="3":
        array[0]= int(array[0])
        array[1]= int(array[1])
    else:
        print("ingrese un numero ")
    if valor in no_cobreescribir:
        print("Ese espacio ya esta ocupado")
        if cual == True:
            poner_x()
            return False
        else:
            poner_circulo()
            return False
    elif  array[0] >=4 or array[1] >=4:
        print("ingrese numeros entre 1 y 3")
        return  False
    elif  array[0] <=0 or array[1] <=0:
        print("ingrese numeros entre 1 y 3")
        return  False
    else:
        return True

def imprimir_matriz():
    for fila in matriz:
        for e in fila:
            print(e, ' ', end='')
        print()
    
def poner_circulo():
    validar = ""
    circulos=input("Ingrese coorenadas para pintar O: ")
    array_circulo = circulos.split(",")
    validar = validar_sobreescrbir(circulos, False, array_circulo)
    if validar == True:
        no_cobreescribir.append(circulos)
        matriz[int(array_circulo[0])-1][int(array_circulo[1])-1]= 0


def poner_x():
    validar=""
    X=input("Ingrese coorenadas para pintar X: ")
    array_x = X.split(",")
    validar = validar_sobreescrbir(X, True, array_x)
    if validar == True:
        no_cobreescribir.append(X)
        matriz[int(array_x[0])-1][int(array_x[1])-1]= "X"


while juego_ganado != True:
    variable="si"
    cont=cont+1
    if cont==6:
        juego_ganado=True

    poner_circulo()
    imprimir_matriz()
    poner_x()
    imprimir_matriz()






