def maior_primo(x):
    cont = 2
    ehNroPrimo = True
 
    while (cont < x and ehNroPrimo):
 
    ehNroPrimo = not ((x % cont) == 0)
    cont += 1

    if ehNroPrimo:
        print(x)
    else:
        
            
