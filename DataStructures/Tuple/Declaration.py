# my_tuple = (10,20,[1,2,3])
# print(id(my_tuple))
# print(type(my_tuple))
# print(type(my_tuple[2]))
# print(type(my_tuple[2][1]))

# my_tuple = (200,)+my_tuple[1:]
# print(my_tuple)
# print(id(my_tuple))

address = 'monty@python.com'
print(type(address))
uname,domain=address.split('@')
print(uname,domain)
