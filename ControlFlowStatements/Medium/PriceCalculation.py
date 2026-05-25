name = input("Enter the name:")
items = int(input("Enter the number of items:"))
if(items >= 100):
    print(name,",",items*7)
elif(items >=10 ):
    print(name,",",items*10)
else:
    print(name,",",items*12)