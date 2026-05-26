# print(dict())

# numbers = dict(x=28,y=10)
# print(numbers)

# numbers1 = dict({'x':90,'y':100})
# print(numbers1)

# numbers2 = dict([('x',45),('y',-23)])
# print(numbers2)

my_fam = {'child1':{'name':'Ram','year':2004},
          'child2':{'name':'Rani','year':2005}}

my_fam['child1']['age']=21

# for i in my_fam:
#     print(i,my_fam[i])

# print(my_fam.keys())
# print(my_fam.values())
# print(my_fam.items())

# print(my_fam.popitem())

# print(my_fam)

# d = {1:'one',2:'two'}

# d1={3:'three'}

# d.update(d1)

# print(d)

# newd = d.copy()
# print(newd)

squares = {x:x*x for x in range(5)}
print(squares)