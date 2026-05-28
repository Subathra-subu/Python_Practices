try:
    file= open("f/test.txt","w")
    try:
        file.write("Hello,Everyone!!!")
    finally:
        print("Content successfully written")
        file.close()
except IOError:
    print("can't find the file")
else:
    print("There is no errors")
finally:
    print("Executed successfully!")