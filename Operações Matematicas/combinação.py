def comb(x,y):
    if y>x:
        print("ERRO")
    else:
        i=1
        fat1=1
        while i<=x:
            fat1=fat1*i
            i=i+1

        j=1
        fat2=1
        while j<=y:
            fat2=fat2*j
            j=j+1

        k=1
        fat3=1
        while k<=(x-y):
            fat3=fat3*k
            k=k+1

    return (fat1)/(fat2*fat3)
