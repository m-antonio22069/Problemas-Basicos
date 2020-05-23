def  insertion_sort(lista):
        fim = len(lista)

        for i in range (fim-1):
            #Inicialmete o menor elemento ja visto é o i-esimo
            pos_minimo=i

            for j in range(i+1, fim):
                if lista[j]<lista[pos_minimo]:
                    pos_minimo=j

            #Coloca o menor elemento achado no inicio da sub-lista
            #Para isso, troca de lugar os elementos da posicao i e pos_minimo
            lista[i], lista[pos_minimo] = lista[pos_minimo], lista[i]

        return lista
