class Student:
    def getStudentInfo(self):
        self.__rollno = input("Enter roll number:")
        self.__name = input("Enter your name:")
    def printStudentInfo(self):
        print("Roll number:",self.__rollno,"\nName:",self.__name)


class Marks(Student):
    def getMarks(self):
        self.getStudentInfo()
        self.__marks1 = float(input("Enter marks for subject1:"))
        self.__marks2 = float(input("Enter marks for subject2:"))
        self.__marks3 = float(input("Enter marks for subject3:"))

    def printMarks(self):
        self.printStudentInfo()
        print("Marks1:",self.__marks1)
        print("Marks2:",self.__marks2)
        print("Marks3:",self.__marks3)
    
    def calcTotalMarks(self):
        return self.__marks1+self.__marks2+self.__marks3

class Result(Marks):
    def getResults(self):
        self.getMarks()
        self.__total = self.calcTotalMarks()
    
    def putResult(self):
        self.printMarks()
        print("Total_Marks:",self.__total)
obj = Result()

obj.getResults()
obj.putResult()