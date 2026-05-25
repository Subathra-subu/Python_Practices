flag = True
sum=0
while(flag):
    price = int(input("Enter the price of the first item:"))
    quantity = int(input("Enter the quantity of the first item:"))
    sum += price*quantity
    want = input("Do you want to enter another item? (yes/no):")
    if(want=="no"):
        break
print("Total Price:",sum)