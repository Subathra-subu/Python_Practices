def Odd_Sum(u_bound,l_bound):
    odd=0;
    for i in range(l_bound,u_bound+1):
        if(i%2!=0):
            odd+=i
    print(odd)
    return odd

def Even_Sum(u_bound,l_bound):
    even=0;
    for i in range(l_bound,u_bound+1):
        if(i%2==0):
           even+=i
    print(even)
    return even

l=int(input("Enter the lower bound:"))
u=int(input("Enter the uppper bound:"))

print("Difference between odd and even sum of numbers:",abs(Odd_Sum(u,l)-Even_Sum(u,l)))