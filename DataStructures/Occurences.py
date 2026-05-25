string = input("Enter the string:")
total_digits=0
total_letters=0
for i in string:
    if i.isnumeric():
        total_digits+=1
    elif i.isalpha():
        total_letters+=1
    else:
        pass
print("Total letters found:",total_letters)
print("Total digits found:",total_digits)
