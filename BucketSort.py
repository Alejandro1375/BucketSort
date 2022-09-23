def seleccion(L):    
    
    for pivote in range(len(L) -1 ):
        min = pivote
        for aux in range(pivote+1,len(L)):
            if L[aux] < L[min]:
                min = aux
        temp =L[min]
        L[min] = L[pivote]
        L[pivote] = temp        
    print(L)
                
         
def cubeta (datos):

    slots = 10
    cubetas = []
    for i in range(0,10,1):
        cubetas.append([])
    
    for index in range(len(datos)):
        num = datos[index]//slots
        cubetas[num].append(datos[index])
    for recorrido in range (len(cubetas)):
        x = seleccion(cubetas[recorrido])
        cubetas[recorrido] = x
datos = [70,12,11,78,40,33,4,31,57,10,41,22,89,88,97,13]
cubeta(datos)
    