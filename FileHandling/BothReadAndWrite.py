file_object = open("test.txt","w")
String = input("Enter the string:")
file_object.writelines(String)
file_object.close()

file = open("test.txt","r")
content = file.read()

for i in content:
    print(i)
file.close()