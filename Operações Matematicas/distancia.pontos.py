import math

x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())

x=math.pow(x1-x2,2)
y=math.pow(y1-y2,2)
d=math.sqrt(x+y)

if d>=10:
    print("longe")
else:
    print("perto")
