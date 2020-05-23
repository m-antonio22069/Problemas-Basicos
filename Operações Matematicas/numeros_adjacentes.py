num=int(input("Digite um número inteiro:"))

a=0
b=1

while num>0 and a!=b:
    a=num%10
    num=(num-a)/10
    b=num%10
if a==b:
    print("sim")
else:
    print("nao")
