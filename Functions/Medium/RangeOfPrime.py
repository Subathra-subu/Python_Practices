def isPrime(num):
    found = True
    for i in range(2,num):
        if(num%i==0): 
            found=False
            break

    return found

start = int(input("Enter the starting number:"))
end = int(input("Enter the ending number:"))
if(start > end): print("Provide valid inputs")
else:
    for i in range(start,end+1):
        if(isPrime(i) and i != 1): 
            print(i)
