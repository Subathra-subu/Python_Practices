def Increment(salary,rating):
    if(rating >= 7.1):
        return salary+ salary*(3/100)
    elif(rating >= 4.1):
        return salary+ salary*(25/100)
    else:
        return salary+ salary*(10/100)


salary = float(input("Enter the salary amount:"))
rating = float(input("Enter the apparaisal rating:"))

if(salary <= 0 or (rating > 10 and rating < 1)):
    print("Invalid Inputs")
else:
    print("Incremented salary:",Increment(salary,rating))
