k=1


while k==1:
    decrescente= True
    anterior = int(input("\nDigite o primeiro valor: "))
    while decrescente == True:
        valor = int(input("\nDigite o proximo termo: "))
        if valor > anterior:
            decrescente = False
        anterior = valor
    print("\nA sequencia não esta mais em ordem decrescente\n")
    print("\nDeseja continuar ? \n 1-Sim   2-Não\n")
    k=int(input())
