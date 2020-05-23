print("informe seu cargo e salario de acordo com a tabela\n 0-Estagiario\n 1-Auxiliar Administrativo\n 2- gerente\n 3-diretor\n 4-analista\n 5-executivo")
print()

a=int(input())

salario=float(input("\n"))

if a==0:
    reajuste=salario*1.1
    print("Seu novo salario será R$%2.f" %reajuste)
elif a==1:
    reajuste=salario*1.2
    print("Seu novo salario será R$%2.f" %reajuste)
elif a==2:
    reajuste=salario*1.3
    print("Seu novo salario será R$%2.f" %reajuste)
elif a==3:
    reajuste=salario*1.4
    print("Seu novo salario será R$%2.f" %reajuste)
elif a==4:
    reajuste=salario*1.55
    print("Seu novo salario será R$%2.f" %reajuste )
elif a==5:
    reajuste=salario*1.6
    print("Seu novo salario será R$%2.f" %reajuste)
else:
    print("\nValor incorreto\n")
    
