print("informe seu cargo e salario de acordo com a tabela\n 0-Estagiario\n 1-Auxiliar Administrativo\n 2- gerente\n 3-diretor\n 4-analista\n 5-executivo")
print()

a=int(input())

if a>=0 and a<=5:
    salario=float(input("\n"))
else:
    print("\nValor incorreto\n")
    exit()
if a==0:
    reajuste=salario*1.1
    
elif a==1:
    reajuste=salario*1.2
    
elif a==2:
    reajuste=salario*1.3
    
elif a==3:
    reajuste=salario*1.4
    
elif a==4:
    reajuste=salario*1.55
    
else:
    reajuste=salario*1.6

print("Seu reajuste salarial é: R$%2.f" %reajuste)


