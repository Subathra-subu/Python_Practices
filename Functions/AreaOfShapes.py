def circle(radius):
    return radius*3.14*3.14

def rectangle(length,breadth):
    return length*breadth

def square(side):
    return side**2

while(True):
    print("Menu")
    print("1.Circle")
    print("2.Rectangle")
    print("3.Squrae")
    print("4.Exit")
    choice = int(input("Enter the choice:"))
    if(choice==1):
        radius = float(input("Enter the radius of circle:"))
        print("Area of Circle:",circle(radius))
    elif(choice==2):
        l = int(input("Enter the length:"))
        b = int(input("Enter the breadth:"))
        print("Area of Rectangle:",rectangle(l,b))
    elif(choice==3):
        side = float(input("Enter the side of square:"))
        print("Area of Square:",square(side))
    elif(choice==4):
        break
    else:
        print("Invalid choice")
