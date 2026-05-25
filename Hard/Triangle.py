import math
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if((a+b)<c or (b+c)<a or (c+a)<b):
    print("Cannot form a triangle")
else:
    s = (a+b+c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area of triangle:",round(area,2))