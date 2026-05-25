def new_salary(salary,hike):
    new_salary = salary+(salary*hike/100)
    print("New salary:",new_salary)

salary = float(input("Enter the per month salary:"))
hike = float(input("Enter the hike amount:"))
new_salary(salary,hike)