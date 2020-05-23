numero= int(input("Digite um numero"))

soma=0

while numero%10 !=0:
    soma = soma + numero%10
    numero//10

print("A soma dos digitos de %d" %numero "é:%d" %soma)

