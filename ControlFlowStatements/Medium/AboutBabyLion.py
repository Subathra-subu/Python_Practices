total = int(input("Enter the total number of animals:"))
rabbit = int(input("Enter the count of rabbit:"))
deer = int(input("Enter the count of deer:"))
birds = int(input("Enter the count of birds:"))
squirrels = int(input("Enter the count of squirrels:"))
sumOfAnimals = rabbit+deer+birds+squirrels
if(total == sumOfAnimals):
    print("Baby lion is well behaved")
elif(total > sumOfAnimals):
    print("Baby lion is mischievous")
else:
    print("Counted wrongly")