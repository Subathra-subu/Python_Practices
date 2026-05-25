num = 2
print(num)
def demo():
    global num
    num = num*2
    print("Local value:",num)
demo()
print("Global value:",num)