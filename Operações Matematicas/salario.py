hora=float(input("digite o valor da hora de trabalho:R$"))
quantidade=int(input("digite a quantidade de horas trabalhadas no mês:"))

salario=hora*quantidade
IR=salario*0.11
INSS=salario*0.08
sindicato=salario*0.05
salario_liquido=salario-IR-INSS-sindicato

print()

print("salario bruto:",salario,"R$")
print("IR(11%):",IR,"R$")
print("sindicato(5%):",sindicato,"R$")
print("salario liquido:",salario_liquido,"R$")
