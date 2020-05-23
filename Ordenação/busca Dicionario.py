def main():
    usuarios = [{'username': 'Lucas','tweets':['Eu adoro bolos','Eu adoro pizza']},
                {'username': 'Bob','tweets':['Eu amo meu gato','Não gosto de futebol']},
                {'username': 'Simon','tweets':[]}]

    print("User:"+busca(usuarios, 'futebol'))

def busca(lista, palavra):
    #Cria uma lista de nomes
    lista_nomes = []

    '''Percorre a lista passada como parametro
    E adiciona os nomes a uma lista''' 
    for i in range(len(lista)):
        lista_nomes.append(lista[i]['username'])

    '''Itera a lista para verificar qual usuario usou a palavra'''
    for i in range(len(lista)):
        '''Cria uma lista de palavras para o usuario i
        e preenche com as mesmas'''
        lista_palavras=[]
        for j in range(len(lista[i]['tweets'])):
            lista_palavras.extend(lista[i]['tweets'][j].split())

        '''Faz a comparação da palavera procurada com
        as palavras existentes'''
        for k in range(len(lista_palavras)):
            if lista_palavras[k] == palavra:
                return lista_nomes[i]
    return 'Ninguem falou isso'

main()
