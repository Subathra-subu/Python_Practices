class circle:
    def __init__(self,radius = 1.0,color = "red"):
        self.__radius = radius
        self.__color = color
    
    def getRadius(self):
        return self.__radius
    def getColor(self):
        return self.__color
    def setRadius(self,radius):
        self.__radius = radius
    def setColor(self,color):
        self.__color=color
    def getArea(self):
        return 3.14*self.__radius*self.__radius
    def __str__(self):
        return f"Circle[radius={self.__radius}, color={self.__color}]"

circle1 = circle()
print(circle1)
circle2 = circle(2.5)
print(circle2)
circle3 = circle(3.5,"blue")
print(circle3)