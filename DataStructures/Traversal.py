greet = 'Welcome'
index=0
while(index < len(greet)):
    print(greet[index],end=" ")
    index=index+1

for i in greet:
    print(i,end=" ")

print(greet[::-2])
print(greet+greet)
print(greet*5)
greet[0]="l"

print (greet)

greeting = "H"+greet[1:]

print(greeting)

txt = "Hard work never fails"
if "work"in txt:
    print("Yes")
else:
    print("No")

greeting = "Hello, World!"
new = "J"+greeting[7:12]
print(new)
new = "J"+greeting[-6:-1]
print(new)

dir(str)