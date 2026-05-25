def add(num1,num2):
    print("Addition of two numbers:",num1+num2)

def sub(num1,num2):
    print("Subtraction of two numbers:",num1-num2)

def multiply(num1,num2):
    print("Multipy of two numbers:",num1*num2)

def calculate(operation,operand1,operand2):
    return operation(operand1,operand2)

num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
calculate(add,num1,num2)
calculate(sub,num1,num2)
calculate(multiply,num1,num2)