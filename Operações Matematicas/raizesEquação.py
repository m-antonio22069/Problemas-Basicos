print("escreva os valores a,b e c da equação do 2º grau")
print()

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
x1=float
x2=float

delta= (b**2)-4*a*c

if delta>=0:
    x1= (-b - (delta**0.5))/(2*a)
    x2= (-b + (delta**0.5))/(2*a)

    print("as raizes da equação são ",x1, " e ",x2)
else:
    print("não existem valores Reais que satisfazem a equação")
