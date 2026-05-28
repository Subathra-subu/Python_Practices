def words(num):
    d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    l = num.split(" ")
    for i in l:
        for x in d:
            val = int(i)
            if(val==x):
                print(d[x],end=" ")
            
num = input("Enter the number:")
words(num)


