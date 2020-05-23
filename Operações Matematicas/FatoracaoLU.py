import numpy as np, random

def fatoraLU(A):
    U = np.copy(A) #Gera uma copia da matriz
    n = np.shape(U)[0] #Gera o numero de linhas da matriz
    L = np.eye(n) #Gera uma matriz identidade com o mesmo numero de linhas de U
    for j in np.arange(n-1): #Operações para a obtenção das matriz L e U
        for i in np.arange(j+1,n):
            L[i,j] = U[i,j]/U[j,j]
            for k in np.arange(j+1,n):
                U[i,k] = U[i,k] - L[i,j]*U[j,k]
            U[i,j] = 0

    #Mostra as matrizes na tela
    for i in range(0,len(L)):
        print(L[i])
    print()
    for i in range(0, len(U)):
        print(U[i])

def matriz(n_linhas, n_colunas):
    matriz = [] # Matriz
    linha = [] # Linha
    dif_zero=0 #define a posição na linha da matriz que é diferente de zero

    # Quando o número de elementos da matriz(linhas) forem diferentes da quantidade máxima definida pelo usuário, ele ficará rodando.
    while len(matriz) != n_linhas:
        if(len(linha)==dif_zero):
            n= random.randint(1,999)
            linha.append(n)
        else:
            n = random.randint(0,999) # Utilizei random para adicionar os valores
            linha.append(n) # Adiciono n à linha

        if len(linha) == n_colunas: # Se a quantidade de elementos for igual à quantidade de colunas definida pelo usuário :
            matriz.append(linha) # Adiciono a linha à matriz
            linha = [] # E zero a "linha" para adicionar outra à matriz
            dif_zero+=1
    return matriz # Retorno da matriz

##################################
##### O PROGRAMA COMEÇA AQUI #####
##################################

num_linhas= int(input("Digite a dimensão da matriz nxn:"))
num_colunas=num_linhas

A=matriz(num_linhas,num_colunas)

E_valido = False

while(E_valido==False):
    determinante= np.linalg.det(A)
    if(determinante!=0):
        for i in range(0, len(A)):
            print(A[i])
        print("\nDetA = {} \n".format(determinante))
        fatoraLU(A)
        E_valido=True
    else:
        A=matriz(num_linhas,num_colunas)

