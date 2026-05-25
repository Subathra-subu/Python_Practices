n = int(input("Enter the number:"))
i=1
sum=0
while(i<=n):
    num = int(input("Enter the number:"))
    if(n==-1):
        break
    else:
        sum+=num
    i=i+1
print("The sum of numbers:",sum)