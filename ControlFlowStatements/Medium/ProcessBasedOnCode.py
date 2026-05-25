code = int(input("Enter the code:"))
if(code==1):
    num1 = float(input("Enter float1 value:"))
    num2 = float(input("Enter float2 value:"))
    print("Sum of float values:",num1+num2)
elif(code==2):
    num1 = int(input("Enter int1 value:"))
    num2 = int(input("Enter int2 value:"))
    print("Product of integer values:",num1*num2)
else:
    string1 = input("Enter string1:")
    string2 = input("Enter string2:")
    print("Concatenation of two strings:",string1+string2)