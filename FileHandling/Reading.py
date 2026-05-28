file = open("test.txt","r")
content = file.readlines()

for line in content:
    words = line.splitlines()
    print(words)

print(content)
file.close()