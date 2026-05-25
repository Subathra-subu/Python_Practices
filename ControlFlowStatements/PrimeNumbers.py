l=int(input("Enter lower limit:"))
u=int(input("Enter upper limit:"))
for i in range(l,u+1):
    if(i==1): continue
    num=i
    for j in range(2,int(num/2)+1):
        if(num%j==0):
            break
    else: print(num)