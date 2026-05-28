file_obj = open("test.txt","w")
# print(file_obj.write("Hey I have started using files in python\n"))
# marks=89
# l = file_obj.write(str(marks))
# print(l)

lines = ["Hello everyone\n","Have a nice day\n","Good day"]
print(file_obj.writelines(lines))
file_obj.close()