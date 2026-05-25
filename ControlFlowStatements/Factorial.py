num = int(input("Enter the number:"))
if(num > 0):
    temp=num
    fact = 1
    while(num > 0):
        fact*=num
        num-=1
    print(f"Factorial of {temp} is ",fact)
elif(num==0):
    print(f"Factorial of {num} is ",1)
else:
    print("Enter a positive number")



