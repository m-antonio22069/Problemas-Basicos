input("ola, bom dia")
lado1= float(input("digite o 1º lado do triangulo "))
lado2=float(input("digite o 2º lado do triangulo "))
lado3=float(input("digite o terceito lado do triangulo "))
sperimetro= (lado1+ lado2+ lado3)/2
area = (sperimetro*(sperimetro-lado1)*(sperimetro-lado2)*(sperimetro-lado3))**0.5
perimetro=2*sperimetro
print("A area do triangulo é:",area,"e o seu perimetro é:",perimetro) 
