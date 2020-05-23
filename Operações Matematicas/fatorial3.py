k=1;

while k==1:
    n=int(input("digite um numero n:"))

    while n<=0:
        print("valor invalido, tente novamente!!")
        n=int(input())
    
    i=1
    fatorial=1
    
    while i<=n:
        fatorial=fatorial*i
        i=i+1
    print("o fatorial de {} é:".format(n),fatorial)
    print("\nDeseja digitar mais um numero?\n  1-SIM   2-NÃO \n")
    k=int(input("\n\t"))

