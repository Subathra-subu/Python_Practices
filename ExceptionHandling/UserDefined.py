class Error(Exception):
    pass
class valueTooSmall(Error):
    pass
class valueTooLarge(Error):
    pass

num = 28

while(True):
    try:
        n = int(input("Enter the guess number:"))
        if(n > num):
            raise valueTooLarge
        elif(n < num):
            raise valueTooSmall
        break
    except valueTooLarge:
        print("The entered value is too large")
    except valueTooSmall:
        print("The entered value is too small")
print("Successfully found the element")