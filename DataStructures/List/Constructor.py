# t = list()
# print(type(t))
# t=['s','u','b','a']

# vowel = "aeiou"
# vowel_list=list(vowel)
# print(vowel_list)

# del vowel_list[2]
# print(vowel_list)

# # del vowel_list
# # print(vowel_list)

# for i in t:
#     print(t)

list1 = ['ken','doe','John','mike']
list2 = [10,90,34,78]

list1.sort()
list2.sort(reverse=True)

print(list1)
print(list2)

list3 = list1.copy()

print(list1 is list3)

list4=list1
print(list4)

list1[1]='Vena'
print(list4)