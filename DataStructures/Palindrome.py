n = input("Enter the String:")
rev = n[::-1]
print(rev)
if(n.__eq__(rev)): # if(n==rev):
    print("Palindrome")
else:
    print("Not a Palindrome")