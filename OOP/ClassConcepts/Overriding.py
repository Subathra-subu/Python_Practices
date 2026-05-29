class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
    def show(self):
        print("Details:",self.name,self.color,self.price)
    def max_speed(self):
        print("Vehicle max speed is 150")
    def gearChange(self):
        print("Vehicle change 6 gear")

class Car(Vehicle):
    def max_speed(self):
        super().max_speed()
        print("Car max speed is 240")
    def gearChange(self):
        super().gearChange()
        print("Car change 7 gear")

car = Car("Wagnor","Green",400000)
car.show()
car.max_speed()
car.gearChange()

vehicle = Vehicle("Truck","Red",200000) 
vehicle.show()
vehicle.max_speed()
vehicle.gearChange()