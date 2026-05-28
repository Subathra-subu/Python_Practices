try:
    num = int(input("Enter the number:"))
    if(num < 0):
       raise ValueError("This is negative number")
except ValueError as e:
    print(e)
finally:
    print("success!!")