l1=[1,2,3,4,5]
choice=0
while(True):
    print("Menu\n1.Append\n2.Insert\n3.Append a list\n4.Modify\n5.Delete From position\n6.Delete element\n7.Ascending order\n8.Descending order\n9.Display\n10.Exit")
    choice=int(input("Enter the choice:"))
    if(choice==1):
        element = int(input("Enter the element to append in the list:"))
        l1.append(element)
    elif(choice==2):
        element = int(input("Enter the element to insert in the list:"))
        pos = int(input("Enter the position to be insert:"))
        if(pos > len(l1)): print("Invalid position")
        else: l1.insert(pos,element)
    elif(choice==3):
        l2=[]
        n=int(input("Enter the number of elements in list:"))
        for i in range(n):
            element=int(input("Enter the element:"))
            l2.append(element)
        l1.extend(l2)
    elif(choice==4):
        element = int(input("Enter the element to modify in the list:"))
        pos = int(input("Enter the position of the element:"))
        l1[pos]=element
    elif(choice==5):
        pos=int(input("Enter the position to be delete:"))
        l1.pop(pos)
    elif(choice==6):
        element = int(input("Enter the element to delete:"))
        l1.remove(element)
    elif(choice==7):
        l1.sort()
    elif(choice==8):
        l1.sort(reverse=True)
    elif(choice==9):
        print(l1)
    elif(choice==10):
        break 