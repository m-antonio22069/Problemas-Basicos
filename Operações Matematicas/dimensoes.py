def dimensoes(minha_matriz):
    linhas = str(len(minha_matriz))
    colunas = str(len(minha_matriz[0]))
    dim = [int(linhas), int(colunas)]

    return dim

def soma_matrizes(m1, m2):
    dim1=dimensoes(m1)
    dim2=dimensoes(m2)
    
    if(dim1==dim2):
        linha = int(len(m1))
        coluna = int(len(m1[0]))
        matriz_soma = []
        for i in range(linha):
            matriz_soma.append([])
            for j in range (coluna):
                soma = m1[i][j] + m2[i][j]
                matriz_soma[i].append(soma)
                
        return matriz_soma
    else:
        return False
