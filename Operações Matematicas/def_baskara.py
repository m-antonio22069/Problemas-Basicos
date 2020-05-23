def delta(a,b,c):
    return b**2-4*a*c

def main():
    a=float(input("digite o valor de a:"))
    b=float(input("digite o valor de b:"))
    c=float(input("digite o valor de c:"))
    imprime_raizes(a,b,c)

def imprime_raizes(a,b,c):
    import math
    if delta(a,b,c)<0:
        print("nao possui raizes reais")
    elif delta(a,b,c)==0:
        x=-b/(2*a)
        print("A unica raiz é:",x)
    else:
        x1=(-b+math.sqrt(delta(a,b,c)))/(2*a)
        x2=(-b+math.sqrt(delta(a,b,c)))/(2*a)
        print("As raizes são:", x1, x2)
