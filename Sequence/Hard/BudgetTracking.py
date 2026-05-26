income = float(input("Enter your monthly income:"))
expense = input("Enter your expenses(space-separated):")
expenses = expense.split(" ")

sum=0.0
for i in expenses:
    sum+= float(i)
print("Budget remaining:$",income-sum)
