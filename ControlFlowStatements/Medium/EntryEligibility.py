age = int(input("Enter the age:"))
if(age < 0 ):
    print("Invalid age")
elif(age <= 10):
    print("Cartoons club")
elif(age <= 20):
    print("Teens club")
else:
    print("Not Eligible")