class Buscador:
    def busca_sequencial(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i]==elemento:
                return i
        return -1

    def busca(self, lista, elemento):
        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <=ultimo:
            meio = (primeiro + ultimo)//2
            print(meio)
            if lista[meio] == elemento:
                return meio
            else:
                if elemento<lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio+1

        return False
