class Student:

    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age

stud = Student("Sham",40)
print('Name:',stud.name,stud.get_age())

stud.set_age(30)

print('Name:',stud.name,stud.get_age())