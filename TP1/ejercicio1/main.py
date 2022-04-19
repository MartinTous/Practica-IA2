from Aestrella import *
import os

#====================== Armar la matriz que representa todo el almacen==================#
def almacen(matriz,dim):
    PF=0             #Pasillo filas
    PC=0             #Pasillos columnas
    estante=0
    for i in range(0,dim):
        matriz.append([0]*dim)

    for i in range(0,dim):
        for j in range(0,dim):
            if PF==0:
                matriz[i][j]=0
            elif PC==0:
                matriz[i][j]=0
            else:
                estante=estante+1
                matriz[i][j]=estante
            PC=PC+1
            if PC==3:
                PC=0
        PF=PF+1
        PC=0
        if PF==5:
            PF=0
    return matriz

#============================= Ubicar posiciones de destino =============================#
# Devuelve las coordenadas de la estantería que solicito
def ubicacion(matriz,pos,dim):
    for i in range(0,dim):
        for j in range(0,dim):
            if matriz[i][j]==pos:
                pos=[i,j]
    return pos




#======================================== MAIN ===========================================#
if __name__=="__main__":
    
    matriz=[]
    print('\n')
    dim=int(input('Tamaño del almacen (LxL) -> L= '))
    matriz=almacen(matriz,dim)                                                              #_Armo la matriz que representa al almacen
    print('\n')
    for i in range(0,dim):                                                                  #_Graficar el almacén
        for j in range(0,dim):
            print(matriz[i][j],end=' ')
        print('\n')

    inicio=ubicacion(matriz,int(input('Posición de inicio: ')),dim)                                                                                                                                                 
    pos1=ubicacion(matriz,int(input('Posición de destino: ')),dim)                          #_Saber el lugar de la matriz de la posicion de destino
    [matriz,camino]=Astar(matriz,inicio,pos1)                                               #_Encontramos el camino óptimo


    os.system('cls')
    print('Camino:\n',camino)
    print('Distancia recorrida: ',len(camino),' celdas')

    print('\n')
    for i in range(0,dim):                                                                 #_Graficar el almacén y el recorrido
        for j in range(0,dim):
            print(matriz[i][j],end=' ')
        print('\n')