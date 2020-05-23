lista_impares = []

def encontra_impares(lista):
    
    if len(lista) ==0:
        return lista_impares
    for i in range(len(lista)):
        if lista[0]%2 != 0:
            lista_impares.append(lista[0])
            return encontra_impares(lista[1:])
        return encontra_impares(lista[1:])
