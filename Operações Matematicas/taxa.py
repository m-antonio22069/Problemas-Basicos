peso=float(input("digite o peso:"))
a=peso-50
taxa=0
if a>=0:
    taxa=4*a
else:
    taxa=0
print()
print("voce deve pagar:",taxa,"reais de taxa")
