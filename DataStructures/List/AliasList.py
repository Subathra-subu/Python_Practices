# def increment(list2):
#     for i in range(0,len(list2)):
#         list2[i]+=5
#     print(list2)
#     print("List2:7",id(list2))

# list1 = [10,20,30,40,50]
# print("Before",list1)
# increment(list1)
# print("After",list1)
# print("List1:",id(list1))

def increment(list2):
    list2=[1,2,3,4,5]
    for i in range(0,len(list2)):
        list2[i]+=5
    print(list2)
    print("List2:",id(list2))

list1 = [10,20,30,40,50]
print("Before",list1)
increment(list1)
print("After",list1)
print("List1:",id(list1))