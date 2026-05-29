class Student:
    def __init__(self):
        self._name = "Python"
    def _funName(self):
        return "Methods here"

class Subject(Student):
    pass

obj = Subject()

print(obj._funName())
print(obj._name)