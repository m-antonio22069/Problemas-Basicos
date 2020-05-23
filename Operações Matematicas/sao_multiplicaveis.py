def dimensoes(minha_matriz):
    linhas = str(len(minha_matriz))
    colunas = str(len(minha_matriz[0]))
    dim = [int(linhas), int(colunas)]

    return dim

def sao_multiplicaveis(m1, m2):
    dim1 = dimensoes(m1)
    dim2 = dimensoes(m2)


    if(dim1[1]==dim2[0]):
        return True
    else:
        return False

