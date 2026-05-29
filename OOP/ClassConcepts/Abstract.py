from abc import ABC,abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def makeSound(self):
        pass

class Dog(Animal):
    def makeSound(self):
        return "Woof!"

class Cat(Animal):
    def makeSound(self):
        return "Meow!!"
    
def print_animal_sound(self):
    print(self.makeSound())

dog = Dog()
cat = Cat()

print_animal_sound(dog)
print_animal_sound(cat)