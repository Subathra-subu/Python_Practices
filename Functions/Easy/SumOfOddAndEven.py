num = int(input("Enter the number:"))
def sum(n):
  odd=even=0
  while(n>0):
    digit = n%10
    n//=10
    if(digit%2==0): even+=digit
    else: odd+=digit
  print("Sum of odd numbers:",odd)
  print("Sum of even numbers:",even)
sum(num)