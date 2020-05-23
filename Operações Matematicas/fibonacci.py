def fibonacci(f,n):

    f[0]=1
    f[1]=1

    for i in range(2,n):
        f[i]=f[i-1]+f[i-2]
        
    return 

def main():
    n=int(input("Digite o numero de termos:"))

    while (n<2):
        n=int(input("Digite o numero de termos"))
    f=[n]
    fibonacci(f,n)

    for i in range(n):
        print(f[i])

    return 0;
