class My_Class:
    def __init__(self,name): #Not support constructor overloading - dynamically type and can variable length arguments
        self.name = name

    def __init__(self,age):
        self.age = age

    def display(self):
        print("Hello,My name is",self.age)

obj1 = My_Class(22)

obj1.display()



